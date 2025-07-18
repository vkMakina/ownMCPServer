# ownMCPServer

## Overview

**ownMCPServer** is a simple Model Context Protocol (MCP) server built with the `mcp` Python package. It provides a set of tools and resources for managing notes.

---

## Technical Details

- **Language:** Python 3.11+
- **Main Dependency:** [`mcp[cli]`](https://pypi.org/project/mcp/) (>=1.9.2)
- **Entry Point:** `main.py`
- **Data Storage:** Notes are stored in a local text file (`notes.txt`).

### Project Structure

```
main.py         # Main server code
notes.txt       # Stores notes (auto-created if missing)
pyproject.toml  # Project metadata and dependencies
README.md       # Project documentation
uv.lock         # Dependency lock file
```

### Core Logic

- **Server Initialization:**  
  The server is created using `FastMCP("AI Notes")`.

- **Notes Management:**  
  - `add_note(note: str)`: Appends a note to `notes.txt`.
  - `list_notes()`: Returns all notes as a string.
  - `get_latest_note()`: Returns the most recent note.
  - `analyze_notes()`: Provides a summary (total notes, total words, average words per note).

- **File Handling:**  
  The server ensures `notes.txt` exists before reading or writing.

---

## How to Run

### 1. Install Python

Ensure you have Python 3.11 or newer installed.  
[Download Python](https://www.python.org/downloads/)

### 2. Install Dependencies

Open PowerShell in the project directory and run:

```powershell
pip install "mcp[cli]>=1.9.2"
```

Or, if you want to use the lock file for reproducible installs:

```powershell
pip install -r requirements.txt
```
*(Note: If `requirements.txt` is not present, use the first command.)*

### 3. Start the MCP Server

Run the following command in PowerShell:

```powershell
python main.py
```

Or, if using the MCP CLI:

```powershell
mcp run main.py
```

### 4. Using the Server

You can interact with the server using MCP-compatible clients or by extending the code with more tools/resources.

---

## Extending the Server

- Add new tools by decorating functions with `@mcp.tool()`.
- Add new resources with `@mcp.resource("resource://name")`.
- Add new prompts with `@mcp.prompt()`.


