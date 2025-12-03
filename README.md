# Note Manager CLI

A command-line application for creating, listing, and searching personal notes. This tool allows users to manage their notes efficiently with simple commands, storing them locally in a JSON file.

![Tests](https://github.com/Alfwarll/is4010-final-note-manager/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [AI-Assisted Development](#ai-assisted-development)
- [License](#license)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Alfwarll/is4010-final-note-manager.git
   cd is4010-final-note-manager

2. Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate      # Windows
    # source venv/bin/activate  # macOS/Linux

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

## Usage

1. Add a new note:
    ```bash
    python src\main.py --add "My Note" "This is the content of my note."

2. List all notes:
    ```bash
    python src\main.py --list
    # Example output:
    # - My Note: This is the content of my note.

3. Search for notes containing a keyword:
    ```bash
    python src\main.py --search "keyword"
    # Example output:
    # No matching notes found.

# Additional Examples

1. Adding multiple notes:
    ```bash
    python src\main.py --add "Shopping List" "Milk, Eggs, Bread"
    python src\main.py --add "Ideas" "Start a YouTube channel"

2. Searching for a keyword
    ```bash
    python src\main.py --search "Eggs"
    # Example output:
    # - Shopping List: Milk, Eggs, Bread

## Features

✅ Add new notes with a title and content

✅ List all saved notes

✅ Search notes by keyword

✅ Stores notes locally in JSON format

✅ Handles duplicate note titles gracefully

✅ Simple and user-friendly CLI interface

## Testing

1. Run all tests locally:
    ```bash
    pytest -v

2. Tests cover:

   ✅ Adding notes

   ✅ Listing notes

   ✅ Searching notes

   ✅ Edge cases like empty titles or missing content

## AI-Assisted Development

This project was developed with assistance from AI tools including GitHub Copilot, ChatGPT, and Gemini. For full details on AI usage, see [AGENTS.md](AGENTS.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


