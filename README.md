![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Infinite Slope Stability Calculator
 
*For geotechnical engineers and engineering geologists: enter soil, slope, and water parameters to calculate the factor of safety for an infinite slope.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geotechnical Engineering
 
This tool computes the factor of safety (FS) against shallow translational sliding for an infinite slope with optional seepage parallel to the slope. The user provides six numeric inputs: effective cohesion c' (kPa, range 0–1000), effective friction angle φ' (degrees, range 0–50), slope angle β (degrees, range 0–90), soil unit weight γ (kN/m³, range 10–30), vertical depth to the potential failure plane z (m, range 0.1–100), and water height above the failure plane h_w (m, range 0 to z). A constant water unit weight γw = 9.81 kN/m³ is used. Logic: convert β and φ' to radians; compute the effective normal stress term σ'_n = (γ · z · cos²β − γw · h_w · cos²β); compute the shear stress term τ = γ · z · sinβ · cosβ; compute FS = (c' + σ'_n · tan φ') / τ. If τ is approximately zero (β = 0), set FS to 999 and report a flat-slope condition with no sliding. Classify FS as: <1.0 Unstable, 1.0–1.25 Marginal, 1.25–1.5 Fair, >1.5 Good. If h_w > z, the UI shows a validation warning and does not compute. The Gradio UI uses a Blocks layout with two columns of three labeled gr.Number inputs each, a Calculate button, and an output area containing a large gr.Number for FS (3 decimal places), a gr.Label for the classification, and a warning banner if FS < 1.0. No AI/ML component is used; this is a deterministic geotechnical calculation.
 
## Run it
 
```bash
docker build -t infinite-slope-stability-calculator .
docker run -p 7860:7860 infinite-slope-stability-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-18.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
