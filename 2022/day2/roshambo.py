p_score_map = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

wld_score_map = {
    "A X": 3, #lose + scissor
    "A Y": 4, #draw + rock
    "A Z": 8, #win + paper
    "B X": 1, #lose + rock
    "B Y": 5, #draw + paper
    "B Z": 9, #win + scissor
    "C X": 2, #lose + paper
    "C Y": 6, #draw + scissor
    "C Z": 7 #win + rock
}

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        return lines 


def calc_p_score(rounds):
    score = 0
    for round in rounds:
        score = score + p_score_map[round] + p_score_map[round[-1]]
    return score

def calc_wld_score(rounds):
    score = 0
    for round in rounds:
        score = score + wld_score_map[round]
    return score


def main():
    rounds = read_input('input.txt')
    total_p_score = calc_p_score(rounds)
    print(f"Total Player Score: {total_p_score}")
    total_wld_score = calc_wld_score(rounds)
    print(f"Total WLD Score: {total_wld_score}")


if __name__ == "__main__":
    main()