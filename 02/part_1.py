from pprint import pprint


def load_puzzle_input(path):
    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    game_results = {}

    for line in file_content.split('\n'):
        if line != '':
            title = line.split(': ')[0]
            game_results[title] = {'rounds': []}
            for rounds in line.split(': ')[1].split('; '):
                result_dict = {}
                for results in rounds.split(', '):
                    result_splits = results.split(' ')
                    result_dict[result_splits[1]] = result_splits[0]

                game_results[title]['rounds'].append(result_dict)

    return game_results


def is_possible(results, config):
    for r in results['rounds']:
        for key in r.keys():
            print(f'{r[key]} : {config[key]}')
            print(int(r[key]) <= int(config[key]))
            if int(r[key]) > int(config[key]):
                return False

    return True


if __name__ == '__main__':
    game_results = load_puzzle_input('puzzle_input.txt')
    configuration = {'red': 12, 'green': 13, 'blue': 14}

    possible_game_numbers = []

    for k, v in game_results.items():
        possible = is_possible(v, configuration)
        if possible:
            possible_game_numbers.append(int(k.split(' ')[1]))

    print(possible_game_numbers)
    print(sum(possible_game_numbers))
