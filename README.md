# PyClaw
A Python CLI for talking to AI models. Inspired by [PicoClaw](https://github.com/sipeed/picoclaw) - built with security, extensibility, and cross-platform support in mind.
---
## Table of Contents
1. [What it does](#what-it-does)
2. [Stack](#stack)
3. [Project structure](#project-structure)
4. [Features](#features)
5. [Getting started](#getting-started)
6. [How it works](#how-it-works)
7. [Upcoming features](#upcoming-features)
8. [Contributing](#contributing)
9. [Maintenance](#maintenance)
---
## What it does
PyClaw gives you a command-line interface for AI conversations - quick one-off queries, back-and-forth chat sessions, and scheduled tasks. Configuration lives in `~/.pyclaw/config.json` and is set up through a guided onboarding flow.
Main use cases:
- Single queries and continuous conversations via Groq
- Scheduled jobs via `cron`
---
## Stack
- **Python 3.8+**
- `pyinputplus` - input validation during onboarding
- `groq` - Groq API
- `keyring` - secure API key storage via OS keychain
- `requests` - LangSearch integration (upcoming)
---
## Project structure
```
pyclaw/
├── __main__.py       # entry point, routes CLI commands
└── src/
    ├── onboard.py    # config setup and personality onboarding
    └── ai.py         # Groq API calls and system prompt builder
```
---
## Features
**Query mode** - ask one question, get one answer, done.

**Chat mode** - back-and-forth conversation that remembers context for the session.

**Onboarding** - walks you through API keys, model settings, tone, response length, and emoji preferences on first run.

**Personality system** - tone, response length, and emoji usage are saved during onboarding and applied consistently across sessions via a system prompt.

**Secure key storage** - API keys are stored in your OS keychain via `keyring`. No plaintext credentials on disk.

**Markdown stripping** - responses are cleaned up for terminal output. No stray `**bold**` leaking into your shell.
---
## Getting started
```bash
git clone https://github.com/venkatram-s/pyclaw.git
cd pyclaw
pip install -r requirements.txt
```
Run onboarding first:
```bash
python __main__.py onboard
```
It asks for your API keys, model name, and how you want the AI to behave. Everything gets saved to `~/.pyclaw/config.json`. API keys are stored separately in your OS keychain.
### Commands
| Command | What it does |
|---|---|
| `python __main__.py onboard` | first-time setup, or reconfigure |
| `python __main__.py query` | single question, single answer |
| `python __main__.py chat` | start a conversation |
| `python __main__.py cron` | manage scheduled tasks |
| `python __main__.py version` | show version |
| `python __main__.py help` | show help |
---
## How it works
`__main__.py` parses the command and routes it. `onboard.py` handles config creation and stores API keys in the OS keychain. `ai.py` builds the system prompt from your personality settings and makes the API call.

The flow is: command -> `__main__.py` -> `src/` module -> Groq -> output to terminal.

A few known limitations worth being upfront about:
- API rate limits apply (Groq)
- Cron jobs don't survive process restarts yet
---
## Upcoming features
- **Cron system** - scheduled job runner with markdown templates and file output
- **LangSearch integration** - wire LangSearch into `ai.py` for web-aware responses
- **Chat session logging** - save conversations to markdown files in `~/.pyclaw/logs/`
---
## Contributing
1. Fork the repo
2. Create a feature branch
3. Open a pull request
Use `pylint` or `flake8` before submitting.
---
## Maintenance
- **Status:** active
- **Maintainer:** [venkatram-s](https://github.com/venkatram-s)
- **License:** unlicensed - contact the maintainer for inquiries
