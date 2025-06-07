import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from scraper import parse_items


def test_parse_items_success():
    html = "<ul><li>Apple</li><li>Banana</li></ul>"
    assert parse_items(html) == ["Apple", "Banana"]


def test_parse_items_non_string():
    with pytest.raises(TypeError):
        parse_items(123)
