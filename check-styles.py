#!/usr/bin/env python3
"""
check-styles.py
Compare each HTML page's inline <style> block against reference-style.css.
Reports CSS property drift so pages can be kept in sync with the reference.

Usage:
    python check-styles.py [--verbose]

    --verbose  also list selectors present in a page but absent from reference
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
REFERENCE = ROOT / "reference-style.css"

# Selectors that every page must define. Missing one of these is always reported.
REQUIRED_SELECTORS = {
    ":root",
    "body",
    "a",
    "a:hover",
    ".btn",
    ".btn:hover",
    ".btn--white",
    ".btn--outline",
    ".btn--red",
    ".btn--outline-dark",
    ".section",
    ".section--gray",
    ".section__inner",
    ".section__label",
    ".section__heading",
    ".section__body",
    ".interest-band",
    ".interest-band__heading",
    ".interest-band__body",
    ".interest-band__ctas",
    "footer",
    "footer .inner",
    ".footer__left p",
    ".footer__left a",
    ".footer__social",
    ".footer__social a",
    ".footer__social a:hover",
    ".footer__social img",
    ".sr-only",
    ".skip-link",
    ".skip-link:focus",
}


def strip_at_rules(text):
    """Remove @-rule blocks (e.g. @media, @keyframes) by tracking brace depth."""
    out = []
    depth = 0
    in_at = False
    for ch in text:
        if ch == "@" and depth == 0:
            in_at = True
        if in_at:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    in_at = False
        else:
            out.append(ch)
    return "".join(out)


def parse_css(text):
    """
    Parse CSS text into {selector: {property: value}}.
    Strips comments and @-rules first.
    Comma-separated selectors are expanded to individual entries.
    """
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    text = strip_at_rules(text)

    result = {}
    for match in re.finditer(r"([^{};]+?)\s*\{([^}]*)\}", text, re.DOTALL):
        selectors_str = match.group(1)
        declarations = match.group(2)

        props = {}
        for decl in declarations.split(";"):
            decl = decl.strip()
            if ":" not in decl:
                continue
            prop, _, val = decl.partition(":")
            prop = prop.strip()
            val = re.sub(r"\s+", " ", val).strip()
            if prop:
                props[prop] = val

        if not props:
            continue

        for sel in selectors_str.split(","):
            sel = re.sub(r"\s+", " ", sel).strip()
            if sel:
                if sel in result:
                    result[sel].update(props)
                else:
                    result[sel] = dict(props)

    return result


def extract_style_block(html):
    """Return the content of the first <style> block in an HTML file."""
    match = re.search(r"<style[^>]*>(.*?)</style>", html, re.DOTALL | re.IGNORECASE)
    return match.group(1) if match else ""


def normalize(value):
    return re.sub(r"\s+", " ", value).strip()


def check_file(html_path, ref_css, verbose):
    html = html_path.read_text(encoding="utf-8")
    style = extract_style_block(html)
    if not style:
        return [f"  WARNING  no <style> block found"]

    page_css = parse_css(style)
    issues = []

    for sel, ref_props in ref_css.items():
        required = sel in REQUIRED_SELECTORS
        present = sel in page_css

        if not present:
            if required:
                issues.append(f"  MISSING  {sel!r}  (required selector)")
            continue

        page_props = page_css[sel]
        for prop, ref_val in ref_props.items():
            page_val = page_props.get(prop)
            if page_val is None:
                if required:
                    issues.append(
                        f"  MISSING  {sel!r} › {prop}\n"
                        f"           reference: {ref_val}"
                    )
            elif normalize(page_val) != normalize(ref_val):
                issues.append(
                    f"  DRIFT    {sel!r} › {prop}\n"
                    f"           reference: {ref_val}\n"
                    f"           page:      {page_val}"
                )

    if verbose:
        for sel in page_css:
            if sel not in ref_css:
                issues.append(f"  EXTRA    {sel!r}  (not in reference)")

    return issues


def main():
    verbose = "--verbose" in sys.argv

    if not REFERENCE.exists():
        print(f"ERROR: {REFERENCE} not found.")
        sys.exit(1)

    ref_text = REFERENCE.read_text(encoding="utf-8")
    ref_css = parse_css(ref_text)

    html_files = sorted(ROOT.glob("*.html"))
    if not html_files:
        print("No HTML files found.")
        sys.exit(0)

    print(f"Checking {len(html_files)} HTML files against {REFERENCE.name}\n")

    total_issues = 0

    for html_path in html_files:
        issues = check_file(html_path, ref_css, verbose)
        if issues:
            total_issues += len(issues)
            print("-" * 60)
            print(f"  {html_path.name}")
            print("-" * 60)
            for issue in issues:
                print(issue)
            print()
        else:
            print(f"  OK  {html_path.name}")

    print()
    if total_issues == 0:
        print("All pages match reference-style.css.")
    else:
        print(f"{total_issues} issue(s) found across {len(html_files)} page(s).")

    sys.exit(1 if total_issues > 0 else 0)


if __name__ == "__main__":
    main()
