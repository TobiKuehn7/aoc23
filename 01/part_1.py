def get_num_from_line(line: str):
    """
    get the first and last number in the string, append the second number to the first and convert to integer
    :param line: one line as string from the input puzzle
    :return: a two-digit number
    """
    nums = []
    for i in line:
        if i.isnumeric():
            nums.append(i)

    return str(nums[0]) + str(nums[-1])


def read_input_puzzle(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    file_content = read_input_puzzle('puzzle_input.txt')
    calibration_values = []
    for line in file_content.split('\n'):
        if line != '':
            calibration_values.append(int(get_num_from_line(line)))

    print(sum(calibration_values))
