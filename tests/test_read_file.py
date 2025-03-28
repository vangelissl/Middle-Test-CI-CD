import pytest
from main import read_file


def test_read_file(prepare_text_file):
    lines = read_file(prepare_text_file)
    assert len(lines) == 10

