

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            row = [char for char in line if char != '\n']
            lines.append(row)
    return lines


def find_scores(forest):
    tree_scores = []
    rows = len(forest)
    cols = len(forest[0])
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            s_up = look_col_up(i,j,rows,forest)
            s_down = look_col_down(i,j,rows,forest)
            s_left = look_row_left(i,j,cols,forest)
            s_right = look_row_right(i,j,cols,forest)
            t_score = s_up*s_down*s_left*s_right
            tree_scores.append(t_score)
    return tree_scores


def look_col_up(row,col,rows,forest):
    score = 0
    for i in range(row-1,-1,-1):
        if forest[row][col] <= forest[i][col]:
            return score+1
        else:
            score += 1
    return score


def look_col_down(row,col,rows,forest):
    score = 0
    for i in range(row+1,rows):
        if forest[row][col] <= forest[i][col]:
            return score+1
        else:
            score += 1
    return score


def look_row_left(row,col,cols,forest):
    score = 0
    for i in range(col-1,-1,-1):
        if forest[row][col] <= forest[row][i]:
            return score+1
        else:
            score += 1
    return score


def look_row_right(row,col,cols,forest):
    score = 0
    for i in range(col+1, cols):
        if forest[row][col] <= forest[row][i]:
            return score+1
        else:
            score += 1
    return score


def main():
    forest = read_input('input.txt')
    scores = find_scores(forest)
    best = max(scores)
    print(best)


if __name__ == "__main__":
    main()