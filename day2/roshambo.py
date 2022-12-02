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

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        return lines 


def calc_score(rounds):
    score = 0
    for round in rounds:
        score = score + p_score_map[round] + p_score_map[round[-1]]
    return score


def main():
    rounds = read_input('input.txt')
    total_p_score = calc_score(rounds)
    print(f"Total Player Score: {total_p_score}")


if __name__ == "__main__":
    main()