import pytest
import os

@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'test.txt')
    with open(target_file, 'w') as file:
        lines = [
            "I went to the park today, it was such a peaceful walk.\n",
            "By the way, have you tried Python programming? It's really fun.\n",
            "I met an old friend on the way back, and we talked for a while.\n",
            "Do you know how to cook a good meal with just a few ingredients?\n",
            "I think 'adventure' is one of those words that makes everything sound exciting.\n",
            "The weather's been so nice lately, perfect for a hike.\n",
            "I was reading a book on Python, and the concepts are really starting to click.\n",
            "Sometimes it's nice to just sit and enjoy the quiet moments.\n",
            "I’ve been looking for a new project, something interesting with Python.\n",
            "It was a regular Tuesday, nothing out of the ordinary, really.\n"
        ]
        file.writelines(lines)
    return target_file


@pytest.fixture(autouse=True)
def prepare_empty_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'empty.txt')
    with open(target_file, 'w') as file:
        lines = []
        file.writelines(lines)
    return target_file