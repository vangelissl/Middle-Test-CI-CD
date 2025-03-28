
def read_file(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    if len(lines) == 0:
        raise ValueError("File is empty")
    return lines


if __name__ == '__main__':
    pass