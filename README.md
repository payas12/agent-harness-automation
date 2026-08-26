# Agent Harness Automation

An AI agent system running on TrueForge that fetches real-time repository trends, executes analytical Python code inside an isolated Daytona sandbox, and enforces human-in-the-loop approvals before file operations.

## Architecture & Features
- **Harness:** TrueForge runtime
- **Sandbox:** Daytona isolated cloud container
- **LLM Engine:** Gemini API
- **Code Quality:** Qodo pull request reviews and static analysis

## Setup Instructions

### 1. Prerequisites
- Node.js 22+
- Python 3.10+
- Daytona API key
- Gemini API key

### 2. Run TrueForge Locally
```bash
npx @truefoundry/trueforge
