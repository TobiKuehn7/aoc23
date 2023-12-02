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


def get_min_config(results):
    min_configuration = {}
    for r in results['rounds']:
        for key in r.keys():
            if key in min_configuration:
                if int(r[key]) > int(min_configuration[key]):
                    min_configuration[key] = int(r[key])
            else:
                min_configuration[key] = int(r[key])

    return min_configuration


def get_multi(min_config):
    res = None
    for k in min_config.keys():
        if res is None:
            res = int(min_config[k])
        else:
            res *= int(min_config[k])

    return res


if __name__ == '__main__':
    game_results = load_puzzle_input('puzzle_input.txt')
    configuration = {'red': 12, 'green': 13, 'blue': 14}

    min_configs = []
    results_of_multiplications = []

    for k, v in game_results.items():
        min_configs.append(get_min_config(v))
        results_of_multiplications.append(get_multi(min_configs[-1]))

    print(sum(results_of_multiplications))
