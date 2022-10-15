"""
I'm a bit lazy so the input file must end with the delimiter
"""
INPUT_FILE = "TAO.txt"
DELIMETER = "-----"
OUTPUT_FOLDER = "chapters"

def write_data_to_file(filename, data=['nothing']):
    # TODO: Strip trailing and leading spaces
    full_path = OUTPUT_FOLDER + "/" + str(filename) + ".txt"
    with open(full_path, 'w') as output:
        for line in data:
            output.write(line)

def empty_line_count(line, current_counter):
    if not line.strip():
        return current_counter + 1
    return 0


with open(INPUT_FILE, 'r') as input:
    i = 0
    data = []
    empty_line_counter = 0
    for line in input:
        empty_line_counter = empty_line_count(line, empty_line_counter)
        if DELIMETER in line or empty_line_counter > 1:
            write_data_to_file(i, data=data)
            i += 1
            empty_line_counter = 0
            data = []
        else:
            data.append(line)

