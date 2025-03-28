import pytest
from main import read_file


def test_read_file_content_exception(prepare_empty_text_file):
    with pytest.raises(ValueError):
        read_file(prepare_empty_text_file)

