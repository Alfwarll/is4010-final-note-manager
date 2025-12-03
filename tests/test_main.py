import os
import sys
import json
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import add_note, list_notes, search_notes, NOTES_FILE

@pytest.fixture(autouse=True)
def run_before_tests():
    # Clean up before each test
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)

def test_add_note():
    add_note("Test", "This is a test note.")
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        notes = json.load(f)
    assert notes[0]["title"] == "Test"
    assert notes[0]["content"] == "This is a test note."

def test_search_notes(capsys):
    add_note("SearchTest", "Find me")
    search_notes("Find")
    captured = capsys.readouterr()
    assert "SearchTest" in captured.out

def test_list_notes(capsys):
    add_note("ListTest", "List me")
    list_notes()
    captured = capsys.readouterr()
    assert "ListTest" in captured.out
