# PyClaw

**PyClaw** is a Python-based AI assistant designed to manage conversational queries and tasks. Inspired by [PicoClaw](https://github.com/sipeed/picoclaw), PyClaw aims to deliver an easy and extensible command-line interface for AI-powered utilities.

---

## **Table of Contents**
1. [Project Summary](#project-summary)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Core Features](#core-features)
5. [Getting Started](#getting-started)
6. [Architecture](#architecture)
7. [Development](#development)
8. [Performance & Scalability](#performance--scalability)
9. [Community & Maintenance](#community--maintenance)
10. [Notable Aspects](#notable-aspects)

---

## **Project Summary**
- **Purpose:** 
  PyClaw facilitates interaction through AI configurations, delivering conversational capabilities with on-demand task scheduling for developers and end-users.
- **Primary Use Cases:**
  - Managing API configurations for Groq and Brave using Python.
  - Delivering single-session conversational AI capabilities.
  - Managing and scheduling tasks using CLI commands (`cron`).
  
---

## **Technology Stack**
- **Language(s):** Python (100%)
- **Libraries and Dependencies:**
  - `pyinputplus`: Input validation for CLI configuration.
  - `groq`: Integration for AI-driven responses.
- **Python Version Requirements:** Python 3.8 or newer.

---

## **Project Structure**
### **Main Directories**
- `src/`: Contains the primary modules for configuration setup and AI integration.
  
### **Key Files**
- `__main__.py`: Entry point of the application; handles CLI commands like `onboard`, `chat`, and `cron`.
- `src/onboard.py`: Manages configuration setup through JSON files for the AI models.
- `src/groq_ai.py`: Interfaces directly with the Groq API for conversational tasks.

---

## **Core Features**
- **Conversational AI Interaction:**
  - Single-query and continuous conversation capabilities with `chat` and `query` commands.
- **Onboarding and Configuration:**
  - Guided CLI setup for API keys, model configurations, and optional parameters.
- **Task Scheduling:**
  - Manage scheduled tasks using a `cron` command.
  
---

## **Getting Started**
### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/venkatram-s/pyclaw.git
   cd pyclaw
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Configuration**
- Use the following command to set up required API keys and parameters:
  ```bash
  python __main__.py onboard
  ```

### **Usage**
PyClaw comes with multiple commands:
- **Onboarding configuration:**
  ```bash
  python __main__.py onboard
  ```
- **Chat functionality:**
  ```bash
  python __main__.py chat
  ```
- **Single query:**
  ```bash
  python __main__.py query
  ```
- **Task scheduling:**
  ```bash
  python __main__.py cron
  ```

---

## **Architecture**
### **Design Patterns**
- Modular CLI structure: distinct modules handle onboarding, AI integration, and command parsing.

### **Component Interaction**
- `__main__.py`: Entry point for all commands.
- `src/onboard.py`: Handles JSON configuration creation.
- `src/groq_ai.py`: Executes AI-related tasks and manages responses.

### **Data Flow**
- Commands are processed through CLI, and required configurations and tasks are delegated to relevant modules.

---

## **Development**
- **To Contribute:**
  1. Fork the repository.
  2. Create a feature branch.
  3. Open a pull request.

- **Testing Approach:**
  - Manually test all commands like `onboard`, `chat`, and `query` for robustness.

- **Code Quality Tools:**
  - Use tools like `pylint` and `flake8` to ensure code quality.

- **CI/CD Pipeline:**
  - Not implemented yet; GitHub Actions can be integrated for automated testing.

---

## **Performance & Scalability**
- **Known Limitations:**
  - Relies on external APIs (Groq/Brave); subject to rate limits.
  - Manual onboarding of configurations.
- **Performance:**
  - Lightweight application but dependent on API response times.
- **Scalability:**
  - JSON-based configuration may not be suitable for larger setups. Transitioning to a database-backed solution could improve scalability.

---

## **Community & Maintenance**
- **Project Status:** Active
- **Maintainer:** [venkatram-s](https://github.com/venkatram-s)

---

## **Notable Aspects**
- **Strengths:**
  - Intuitive command-line interface and onboarding process.
  - Simple, extensible architecture.

- **Areas for Improvement:**
  - Automate onboarding to detect and reuse existing environments.
  - Better CLI error handling for interrupted processes.

- **Comparison with Alternatives:**
  - Unlike heavier AI assistant systems, PyClaw is lightweight and highly developer-friendly.

---
### License
This repository is currently not licensed. Please contact the maintainer for licensing inquiries.
