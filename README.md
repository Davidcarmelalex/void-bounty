# VOID.Bounty

> Let us hack you before they do.

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Next.js](https://img.shields.io/badge/Next.js-16-black)](https://nextjs.org)
[![Part of](https://img.shields.io/badge/MrNothing-Movement-purple)](https://github.com/Davidcarmelalex/MrNothing)

**VOID.Bounty** is an agentic bug bounty platform powered by the MrNothing movement — fully automated, AI-driven vulnerability discovery and triage.

---

## How It Works

```
Company defines scope → Hunters (human + AI) submit reports
       → AI triage agent scores severity
       → Auto-validated reports pay out instantly
       → Resolved vulnerabilities close automatically
```

---

## Architecture

```
void-bounty/
├── src/app/
│   ├── page.tsx              Program listings
│   ├── program/[id]/         Program detail + submit
│   ├── dashboard/            Hunter dashboard
│   └── admin/                Company program management
├── agents/
│   └── triage.py             AI vulnerability triage agent
├── lib/
│   └── severity.ts           CVSS-based severity scoring
└── tests/
```

---

## Severity Levels

| Level | CVSS Range | Response Time |
|-------|-----------|---------------|
| Critical | 9.0–10.0 | 24h |
| High | 7.0–8.9 | 72h |
| Medium | 4.0–6.9 | 7 days |
| Low | 0.1–3.9 | 30 days |
| Informational | 0.0 | Acknowledged |

---

## Stack

Next.js 16 · TypeScript · Tailwind CSS 4 · Python triage agent · FastAPI · PostgreSQL

---

## Quick Start

```bash
git clone https://github.com/Davidcarmelalex/void-bounty
cd void-bounty && npm install
cp .env.example .env.local && npm run dev
```
