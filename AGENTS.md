# AI-Assisted Development Documentation

## AI Tools Used
- **GitHub Copilot**: Generated boilerplate code for CLI commands and helper functions.
- **ChatGPT**: Assisted in writing tests, handling edge cases, and debugging errors.
- **Gemini**: Helped with project planning and CLI feature design.

## Example Prompts and Results

### Planning
**Prompt:** "Design a Python CLI note manager. Suggest features and file structure."  
**Result:** Recommended add/list/search notes, use `argparse`, store notes in JSON, include tests.

### Implementation
**Prompt:** "Write a function to add a note to a JSON file with error handling."  
**Result:** Provided a working Python function handling duplicate notes and empty titles.

### Testing
**Prompt:** "Write pytest tests for add_note, list_notes, and search_notes functions."  
**Result:** Generated `test_main.py` covering valid input, edge cases, and empty searches.

### Debugging
**Prompt:** "Getting ModuleNotFoundError when importing src in pytest."  
**Result:** Suggested adding `__init__.py` in `src` and using `PYTHONPATH` for imports.

## Reflection

### What Worked Well
- Copilot saved time on repetitive boilerplate code.
- ChatGPT helped with test design and debugging.
- AI guidance clarified proper project structure and module imports.

### Challenges
- Some AI suggestions were overly complex and needed simplification.
- Required verification of library availability and Python version compatibility.

### Learning Impact
Using AI strategically made development faster without skipping learning. It helped focus on understanding logic and architecture while automating repetitive tasks.
