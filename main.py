
def read_file(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    if len(lines) == 0:
        raise ValueError("File is empty")
    return lines

def filter_lines_by_word(lines, word):
    filtered_lines = [line for line in lines if word.lower() in line.lower()]
    return filtered_lines

if __name__ == '__main__':
    pass