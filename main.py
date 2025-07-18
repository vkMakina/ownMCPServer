# server.py
from mcp.server.fastmcp import FastMCP
import os
from starlette.applications import Starlette
from starlette.routing import Mount

import uvicorn

# Create an MCP server
mcp = FastMCP("AI Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")


def ensure_notes_file():
    """Ensure the notes file exists."""
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'w') as f:
            f.write("")


@mcp.tool()
def add_note(note: str) -> str:
    """Add a note to the notes file.
    Args:
        note (str): The note to add.
    Returns:
        str: Confirmation message.
    """
    ensure_notes_file()
    with open(NOTES_FILE, 'a') as f:
        f.write(note + "\n")
    return f"Note added: {note}"


@mcp.tool()
def list_notes() -> str:
    """List all notes from the notes file.
    Returns:
        str: All notes as a string.
    """
    ensure_notes_file()
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    return notes or "No notes found."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """Get the latest note from the notes file.
    Returns:
        str: The latest note or a message if no notes exist.
    """
    ensure_notes_file()
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    return notes[-1].strip() if notes else "No notes found."


@mcp.prompt()
def analyze_notes() -> str:
    """Analyze the notes and return a summary.
    Returns:
        str: A summary of the notes.
    """
    ensure_notes_file()
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    
    if not notes:
        return "No notes to analyze."
    
    # Simple analysis: count words in each note
    word_counts = [len(note.split()) for note in notes]
    total_words = sum(word_counts)
    return f"Total notes: {len(notes)}, Total words: {total_words}, Average words per note: {total_words / len(notes):.2f}"


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

app = Starlette(
    debug=True,
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport="streamable-http")
   