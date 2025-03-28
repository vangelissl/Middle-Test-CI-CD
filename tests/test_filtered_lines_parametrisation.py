import pytest
from main import filter_lines_by_word


@pytest.mark.parametrize("lines, word, expected_number", [
    ([
        "I went to the park today it was such a peaceful walk",
        "By the way have you tried Python programming Its really fun",
        "I met an old friend on the way back and we talked for a while"
    ], "Python", 1),

    ([
        "The quick brown fox jumped over the lazy dog",
        "A quick wit can solve many problems"
    ], "quick", 2),
])
def test_filter_lines_by_word(lines, word, expected_number):
    result = filter_lines_by_word(lines, word)
    assert len(result) == expected_number

