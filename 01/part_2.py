import re


def get_num_from_line(line: str):
    nums_in_letters = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    nums = {}
    for i in range(0, len(line)):
        if line[i].isnumeric():
            nums[i] = line[i]

    for k, v in nums_in_letters.items():
        try:
            matches = re.finditer(k, line)
            for match in matches:
                nums[match.start()] = v
        except ValueError:
            continue

    sorted_results = sorted(nums.items())

    return str(sorted_results[0][1]) + str(sorted_results[-1][1])


def read_input_puzzle(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':

    file_content = read_input_puzzle('puzzle_input.txt')
    calibration_values = []
    for file_line in file_content.split('\n'):
        if file_line != '':
            calibration_values.append(int(get_num_from_line(file_line)))

    print(sum(calibration_values))
