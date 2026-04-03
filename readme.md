# 🐍 Python for JavaScript Developers

![Prerequisite](https://img.shields.io/badge/Prerequisite-JavaScript%20Fullstack-blue)
![Type](https://img.shields.io/badge/Type-Learning%20Course-brightgreen)
![Focus](https://img.shields.io/badge/Focus-Python%20Ecosystem-yellow)
![Covers](https://img.shields.io/badge/Covers-Backend%20%7C%20APIs%20%7C%20Automation%20%7C%20AI-informational)
![Outcome](https://img.shields.io/badge/Outcome-Multi--Language%20Engineer-purple)

> **A A hands-on course for JavaScript fullstack developers who are ready to think beyond the Node ecosystem.**

You already know how to build things. You've shipped APIs, wired up databases, and reasoned through fullstack architecture. This course isn't about learning to code — it's about learning a second language and unlocking a completely different part of the industry.

```
  JavaScript                          Python
  ──────────────────────────          ──────────────────────────
  ✓ Browser / frontend                ✓ Machine learning & AI
  ✓ DOM & UI interactions             ✓ Data science & analytics
  ✓ Real-time & event-driven          ✓ Automation & scripting
  ✓ React, Vue, Angular               ✓ Data pipelines & ETL
  ✓ Backend web (Node/Express)        ✓ Scientific computing
                                      ✓ Backend web (Django/FastAPI/Flask)
                                      ✓ Backend AI & data tooling

  JavaScript owns the browser.
  Python owns data, AI, and science.
  Both compete on the backend.
```

## 🎯 What This Course Is

This is a **practical, developer-focused course** that teaches Python the way a JS developer actually needs to learn it — by mapping everything to what you already know and being direct about where the two ecosystems differ.

**The ecosystem difference** — Python and JavaScript have completely different tooling, package management, and environment setup. Coming in assuming they work the same way is the fastest way to get stuck. This course explains the differences directly and maps every concept to something you already know.

**Building the same things, differently** — You'll build backend apps in Python that you've already built in Node — APIs, data processors, server-side scripts — so you can see exactly how the two languages compare on familiar ground.

**Building things JavaScript can't do easily** — Automation scripts, data pipelines, web scrapers, and AI-integrated tools. These are things Python does better than any other language, and you'll build real working versions of them.

**Understanding when to use which** — By the end you'll be able to look at a project and make an informed decision about whether it belongs in Node or Python, and why.

## ⚖️ Where JavaScript Still Wins

This course is honest about tradeoffs. Python is not the right tool for everything, and knowing when *not* to use it is part of becoming a better engineer.

**Browser execution.** Python does not run natively in the browser. If it runs in a browser, it's JavaScript — full stop. WebAssembly projects like Pyodide exist, but this is not a production pattern.

**Real-time & event-driven UIs.** Node's non-blocking I/O model and React's component paradigm are purpose-built for interactive UIs. Python's async story (`asyncio`) is capable, but it's not where the ecosystem shines.

**Full-stack in one language.** With Node/Express on the backend and React on the frontend, you can stay in JavaScript end-to-end. Python forces a language boundary — your frontend is still JavaScript regardless.

**Startup ecosystem defaults.** Most early-stage product backends default to Node, not Python, simply because frontend devs can contribute. Python backends (Django, FastAPI, Flask) are common in data-heavy products but are not the default for generic web apps.

> Knowing this isn't a reason to avoid Python — it's a reason to understand exactly where it fits.


## ✅ Prerequisites

This course moves fast and skips the basics. You should already be comfortable with:

- JavaScript (ES6+) and how it works in the browser and on the server
- Building REST APIs with Node.js and Express or similar
- Working with databases, routes, and server-side logic
- The command line and managing project files

## 📂 Course Structure

```
python-for-js-devs/
├── 01-environment/        ← venv, pip, VS Code setup — the ecosystem explained
├── 02-fundamentals/       ← Python syntax mapped to JS concepts you know
├── 03-backend/            ← building APIs in Flask and FastAPI vs Express
├── 04-automation/         ← scripts, file processing, scheduled tasks
├── 05-data-and-scraping/  ← working with HTML, APIs, and structured data
└── 06-ai-integration/     ← connecting Python to ML libraries and AI APIs
```

Each module builds on the previous one. Start at `01-environment` and work through in order.

## 🚀 What You'll Walk Away With

By the end of this course you will:

- Set up and manage a Python project from scratch
- Read and write Python confidently without constantly looking things up
- Build backend APIs in Python and understand how they compare to Node
- Write automation and data processing scripts that would be painful in JS
- Understand the Python AI and data ecosystem and why it dominates
- Make informed decisions about when to reach for Python vs JavaScript

## 💡 The Core Idea

Learning Python as a JS developer isn't about starting over. The fundamentals you already have — how servers work, how data flows, how to structure logic — transfer directly. The syntax is different. The ecosystem is different. The mental model is mostly the same.

> The goal isn't to replace JavaScript. It's to become an engineer who can move between ecosystems and pick the right tool for the job.

## 🛠️ Getting Started

Head to [`01-environment`](./01-environment/) to get your Python environment set up. If you've never used Python before, don't skip this — the environment works very differently from Node and it's worth understanding before writing a single line of code.

## License

![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)

**© 2026 Frank Stepanski. All Rights Reserved.**  
This repository is protected under a custom proprietary license.  
Forking and cloning are permitted for personal study only.  
No redistribution, publication, modification, or teaching use is allowed.  

See the [LICENSE](./LICENSE.md) file for all terms and restrictions.
