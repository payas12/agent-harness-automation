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

**For Mac/Linux users (with Node 22+ installed natively):**
```bash
npx @truefoundry/trueforge
```

**Windows / Docker Fallback (Recommended):**
If you encounter environment path errors on Windows, run the agent harness inside a Node 22 Alpine container:
```bash
docker run -it --name trueforge -p 8790:8790 -e HOST=0.0.0.0 -v trueforge_data:/root/.trueforge node:22-alpine npx -y @truefoundry/trueforge
```
Once initialized, open `http://localhost:8790` or `http://127.0.0.1:8790` in your browser.

### 3. Configure Providers
- **Models:** Add your Gemini API key under **Settings → Models**.
- **Sandbox:** Add your Daytona API key under **Settings → Sandbox providers**.

### 4. Execute the Agent
Use the chat interface to query trends or execute custom scripts safely in Daytona.

---

## Qodo Code Review Evidence

- **Merged PR:** https://github.com/payas12/agent-harness-automation/pull/1
- **Findings & Actions:** Qodo surfaced a High-severity reliability finding regarding exit codes on errors and a Medium-severity issue concerning missing network timeouts. Both were resolved in commit `714f827` before merging to `main`.
