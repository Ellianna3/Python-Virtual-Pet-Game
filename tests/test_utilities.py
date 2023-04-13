from python_virtual_pet import utilities
from pytest import MonkeyPatch as monkeypatch
from io import StringIO

def test_get_menu_choice_for_legitimate_output(monkeypatch):
    menu = "Options: 1, 2, or 3"
    legal_choices = ("1", "2", "3")
    number_input = StringIO('2\n')
    monkeypatch.setattr('sys.stdin', number_input)
    result = utilities.get_menu_choice(menu, legal_choices)
    assert result in legal_choices

def test_get_menu_choice_for_2wrongs_and_1right(monkeypatch):
    menu = "Options: 1, 2, or 3"
    legal_choices = ("1", "2", "3")
    number_input = StringIO('12\n22\n3\n')
    monkeypatch.setattr('sys.stdin', number_input)
    result = utilities.get_menu_choice(menu, legal_choices)
    assert result in legal_choices