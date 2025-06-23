
# ClearPath Safety Assistant – Version History & Changelog

## 🆕 Version 2 – “Consultant Edition” (Current)
**Release Date:** June 2025  
**Project Folder:** `clearpath-safety-assistant-v2`

### 🔧 Major Changes from v1:
- 🔀 **Two user roles:** Introduced **Assist Mode** (plain-language for business users) and **Consultant Mode** (technical responses for insurance producers and safety pros)
- 🧠 **Updated prompts**:
  - Consultant mode trained to understand EHS, property/casualty, and workers’ comp risk management
  - Assist mode focused on nonprofits, small business owners, and schools
- 🎨 **New branding**:
  - Replaced shield icon with ClearPath logo
  - Applied branded color scheme (`F3F1EC` background, `#1B4D3E` primary)
- 🌐 **Query-based routing**:
  - `?mode=assist` or `?mode=consultant` to auto-load correct mode (toggle hidden)
- 📝 **New UI logic**:
  - Descriptions updated to reflect user role
  - Consultant toggle hidden in Assist Mode for simplicity
- 📦 Folder restructured for local use and easier deployment:
  - `.streamlit/config.toml` added
  - `secrets.toml` support for local dev
  - `media/` folder for logos and assets

---

## ✅ Version 1 – MVP Beta
**Release Date:** Early June 2025  
**Project Folder:** `clearpath-safety-assistant`

### Features:
- Single prompt system for general safety and compliance questions
- Streamlit deployment for small business and safety consultant use
- Plain layout with red accent and no logo
- Integrated OpenAI GPT-4 with basic API setup
- Embedded on ClearPath’s Framer site for early testing

---

## 🛠 Planned (v3 and Beyond)
- 🧾 Paywall integration for program templates
- 📁 Downloadable customized safety plans/checklists
- 🔐 SOC 2 readiness and disclaimer UI
- 📊 Admin dashboard to monitor usage metrics

## ⚠️ License & Usage

This assistant is currently in closed beta and not available for public use or redistribution.  
All intellectual property, code, and brand assets are owned by **Antolik Consulting Group LLC (ClearPath Safety Solutions)**.

Use is limited to approved testers and client partners under written agreement.  
Commercial licensing will be available upon official launch.  

📩 For inquiries, contact: [sean@clearpathsafetysolutions.com](mailto:sean@clearpathsafetysolutions.com)
