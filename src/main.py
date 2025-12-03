import argparse
import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4)

def add_note(title, content):
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    print(f"✓ Note '{title}' added.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    for note in notes:
        print(f"- {note['title']}: {note['content']}")

def search_notes(keyword):
    notes = load_notes()
    results = [note for note in notes if keyword.lower() in note["title"].lower() or keyword.lower() in note["content"].lower()]
    if not results:
        print("No matching notes found.")
        return
    for note in results:
        print(f"- {note['title']}: {note['content']}")

def main():
    parser = argparse.ArgumentParser(description="Markdown Note Manager CLI")
    parser.add_argument("--add", nargs=2, metavar=("title", "content"), help="Add a new note")
    parser.add_argument("--list", action="store_true", help="List all notes")
    parser.add_argument("--search", metavar="keyword", help="Search notes by keyword")
    args = parser.parse_args()

    if args.add:
        add_note(args.add[0], args.add[1])
    elif args.list:
        list_notes()
    elif args.search:
        search_notes(args.search)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
