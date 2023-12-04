def get_input_puzzle(path):
    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    winning_number_list = []
    my_number_list = []
    for line in file_content.split('\n'):
        if line != '':
            winning_numbers, my_numbers = line[10:].split(' | ')

        w_n_tmp = []
        m_n_tmp = []

        for n in winning_numbers.split(' '):
            if n != '':
                w_n_tmp.append(int(n))

        for n in my_numbers.split(' '):
            if n != '':
                m_n_tmp.append(int(n))

        winning_number_list.append(w_n_tmp)
        my_number_list.append(m_n_tmp)

    return winning_number_list, my_number_list


def calc_points(winning_nums, my_nums):
    scores = []
    for card in range(0, len(winning_nums)):
        card_score = 0
        for mine in my_nums[card]:
            for winning_num in winning_nums[card]:
                if mine == winning_num:
                    if card_score == 0:
                        card_score = 1
                    else:
                        card_score = card_score * 2

        scores.append(card_score)

    return scores


if __name__ == '__main__':
    winning, mine = get_input_puzzle('puzzle_input.txt')
    points = calc_points(winning, mine)
    print(sum(points))
