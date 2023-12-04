def get_puzzle_input(path):
    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    lines = []
    for line in file_content.split('\n'):
        elements = []
        for i in line:
            elements.append(i)
        lines.append(elements)

    return lines


def get_symbols(puzzle: list):
    symbols = []
    for line in puzzle:
        for element in line:
            if (not str(element).isnumeric()) and element != '.' and element not in symbols:
                symbols.append(element)

    return symbols


def get_all_numbers(puzzle: list):
    numbers = {'numbers': []}
    for line in range(0, len(puzzle)):
        number = {'number': ''}
        for element in range(0, len(puzzle[line])):
            if str(puzzle[line][element]).isnumeric():
                if len(number['number']) == 0:
                    number['start'] = element
                    number['line'] = line

                number['number'] += str(puzzle[line][element])
            else:
                if len(number['number']) > 0:
                    number['end'] = element - 1
                    numbers['numbers'].append(number)
                    number = {'number': ''}

            if element == len(puzzle[line]) - 1:
                number['end'] = element
                if number['number'] != '':
                    numbers['numbers'].append(number)
                number = {'number': ''}

    return numbers


def calc_search_area(line, start, end, x_size, y_size):
    start_line = line - 1
    start_elem = start - 1
    stop_line = line + 2
    stop_elem = end + 2

    if start_line < 0:
        start_line = 0
    if start_line > y_size:
        start_line = y_size + 1
    if start_elem < 0:
        start_elem = 0
    if start_elem > x_size:
        start_elem = x_size + 1

    if stop_line < 0:
        stop_line = 0
    if stop_line > y_size:
        stop_line = y_size
    if stop_elem < 0:
        stop_elem = 0
    if stop_elem > x_size:
        stop_elem = x_size

    return (start_line, start_elem), (stop_line, stop_elem)


def get_search_areas_for_numbers(puzzle: dict, puzzle_x_size, puzzle_y_size):
    for number in puzzle['numbers']:
        top_left, bottom_right = calc_search_area(number['line'], number['start'], number['end'],
                                                  puzzle_x_size, puzzle_y_size)

        number['s_start'] = top_left
        number['s_end'] = bottom_right

    return puzzle


def check_if_valid(number, puzzle, symbol_list):
    print(number)
    for row in range(number['s_start'][0], number['s_end'][0]):
        for element in range(number['s_start'][1], number['s_end'][1]):
            for symbol in symbol_list:
                try:
                    print(f'element: {puzzle[row][element]}')
                    print(symbol)
                    if puzzle[row][element] == symbol:
                        print('FOUND')
                        return True
                except IndexError:
                    continue

    return False


def find_valid_numbers(areas, puzzle, symbol_list):
    valid_numbers_list = []
    i = 0
    for number in areas['numbers']:
        if i <= 25:
            if check_if_valid(number, puzzle, symbol_list):
                valid_numbers_list.append(int(number['number']))
            #i += 1
        else:
            break
    return valid_numbers_list


if __name__ == '__main__':
    input_puzzle = get_puzzle_input('puzzle_input.txt')
    #input_puzzle = get_puzzle_input('example.txt')
    puzzle_x = len(input_puzzle)
    puzzle_y = len(input_puzzle[0])

    symbols = get_symbols(input_puzzle)

    # this solution is probably the most inefficient way to solve this, but I just want to try it and maybe build a more
    # efficient one later for comparing them

    numbers = get_all_numbers(input_puzzle)
    print(numbers)
    search_areas = get_search_areas_for_numbers(numbers, puzzle_x, puzzle_y)

    valid_numbers = find_valid_numbers(search_areas, input_puzzle, symbols)
    print(valid_numbers)
    print(sum(valid_numbers))
