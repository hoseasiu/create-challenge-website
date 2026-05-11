---
title: "Software"
url: https://beaver-works-assistive-tech.mit.edu/create-challenge/create-course/maker-skills/software
snapshot_date: 2026-05-11
content_status: full
nav_parent: "Maker Skills"
---

# Software

## Software Development

Software-focused projects in the CRE[AT]E Challenge typically take one of four forms:

1. **Web/webapp** — public or just for the co-designer
2. **Desktop software** — non-web
3. **Mobile app** — iOS or Android
4. **MCU/SBC software** — for microcontroller units (Arduino, BeagleBone) or single-board computers (Raspberry Pi, NVIDIA Jetson) to interface with sensors and actuators

---

## Version Control

**[GitHub](https://github.com/)** — code repository for tracking changes and collaborating. Can host websites via [GitHub Pages](https://pages.github.com/). The [GitHub Student Developer Pack](https://education.github.com/pack) provides access to many additional resources.

Teams writing significant code should use GitHub for version control.

---

## User Interface and Front-End Development

Must consider the user interface regardless of whether the product has a visual interface. Some interactions are contained (desktop skill-practice app); others involve the user, software, and external environment (medication reminders, clothing choice aids).

For software with a visual UI: consider what "pages" or states the user is in and how they transition.

**[Figma](https://www.figma.com/)** — popular app for creating framework prototype mockups (wireframes) of an app or website without building all features. Free for students and educators. Recommended as a starting point for prototyping front-ends.

---

## Web Development

*(Page notes this section is TODO — learning resources to be added)*

- Mobile viewport simulation: [Chrome DevTools device mode](https://developer.chrome.com/docs/devtools/device-mode)

---

## Desktop Software Development

Most general kind of development with the broadest set of resources.

### Packaging

Packaging bundles software — executables, libraries, configuration, metadata — into a structured format for deployment (e.g., `.msi`, `.exe`, `.msix` on Windows, `.dmg` on macOS).

**Why packaging matters:**
1. **Different environments** — development machine has the right libraries; user's laptop likely doesn't
2. **Dependency management** — packaged apps detail their dependencies
3. **Consistent installs** — uniform behavior across users; supports automation, version control, uninstall cleanliness
4. **Security & isolation** — modern formats like MSIX on Windows grant package identity for system services (e.g., notifications)

---

## Mobile Application Development

### iOS Development

Currently behind significant barriers:
1. Must own a Mac for development
2. Apple Developer Account required ($99/year per user)
3. Must know Swift or Objective-C

**Recommendation:** Unless already familiar with iOS dev and willing to pay costs, build a webapp instead that the co-designer can access from their phone.

### Android Development

Far more accessible:
- Can develop on any computer using Java or Kotlin
- [Android Developers getting started guide](https://developer.android.com/get-started/overview)
- [CodingWithMitch](https://codingwithmitch.com/) — tutorials and example projects

### Visual Programming for Mobile: MIT App Inventor

**[MIT App Inventor](https://appinventor.mit.edu/)** — intuitive, visual (drag-and-drop) programming environment for building fully functional apps for Android phones, iPhones, and tablets. iOS still requires a developer license to deploy.

**Best for:**
1. **Rapid Prototyping** — quickly create and test app ideas; no extensive coding skills required
2. **IoT and Hardware Integration** — connects mobile apps with Arduino/Raspberry Pi for sensor data, home automation, remote control

**Useful links:**
- [System Requirements](https://appinventor.mit.edu/explore/content/system-requirements)
- [Documentation](https://appinventor.mit.edu/explore/library)
- [App of the Month Gallery](https://appinventor.mit.edu/explore/app-month-gallery)

---

## Software Accessibility Considerations

- **Screen-reader accessibility** — check that images have descriptive alt text
- **Color and contrast** — important for low-vision and colorblind users
  - [Adobe article on color contrast for accessibility](https://xd.adobe.com/ideas/principles/web-design/color-contrast-considerations-accessibility-design/)
  - [randoma11y.com](https://www.randoma11y.com/) — generates accessible color palettes with contrast checking
  - [accessiBe's accessScan](https://accessibe.com/accessscan) — checks website WCAG compliance
  - Firefox has a [built-in colorblindness simulator](https://www.youtube.com/watch?v=eBefjaWud-M) in its Accessibility Inspector

---

## AI and Machine Learning Tools for Accessibility

AI/ML tools are increasingly popular for student projects.

An embedded YouTube video covers the **machine learning life cycle** — from initial conception to deployment.

**[HuggingFace](https://huggingface.co/)** — common platform for getting trained ML models and datasets. See their [documentation page](https://huggingface.co/docs) for getting started.

### Data Bias and Disability

Critical consideration in AT: **dataset biases may work against you**.

Example: Emotion recognition via computer vision for autism/neurodivergence.
- If recognizing emotions of **neurotypical individuals** → standard datasets work
- If recognizing emotions **of your co-designer** → public datasets may be insufficient; fine-tuning with co-designer-specific data may be necessary

**Rule of thumb:** If the model's input is NOT affected by the co-designer's disability (e.g., household objects), public datasets may be fine. If the input IS affected by the disability (facial expressions, vocalizations), you likely need co-designer-specific fine-tuning.

Example: [The OpTECHs](https://beaver-works-assistive-tech.mit.edu/create-challenge/2023-projects-section/2023-project-page-the-optechs) used visually identifying Uno cards and collected dataset data from their school.

### Training Models

Don't train from scratch unless necessary. Try to get an existing model and use it (see HuggingFace).

For fine-tuning / data collection and labeling:
- Manual annotation on your own computer
- **[CVAT](https://www.cvat.ai/)** — online platform for dataset annotation
- **[Teachable Machine](https://teachablemachine.withgoogle.com/)** — graphical interface for annotating datasets and automated workflows

### Other Resources
- If using App Inventor: [example AI projects with App Inventor](https://appinventor.mit.edu/explore/ai-with-mit-app-inventor)
