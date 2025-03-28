import os
from main import write_to_file


def test_write_to_file(tmp_path):
    lines = [
        "Hello, this is a test line.\n",
        "This is another line to test the write functionality.\n",
        "Python is fun to work with!\n"
    ]

    target_file = os.path.join(tmp_path, 'test_write.txt')

    write_to_file(lines, target_file)

    with open(target_file, 'r') as file:
        file_content = file.readlines()

    assert file_content == lines

