

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            row = [char for char in line if char != '\n']
            lines.append(row)
    return lines


def find_viz(forest):
    viz_count = 0
    rows = len(forest)
    cols = len(forest[0])
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if look_col_up(i,j,rows,forest):
                viz_count += 1
                continue
            if look_col_down(i,j,rows,forest):
                viz_count += 1
                continue
            if look_row_left(i,j,cols,forest):
                viz_count += 1
                continue
            if look_row_right(i,j,cols,forest):
                viz_count += 1
                continue
    return viz_count


def look_col_up(row,col,rows,forest):
    viz = True
    for i in range(0,row):
        if forest[row][col] <= forest[i][col]:
            viz = False
            return viz
    return viz


def look_col_down(row,col,rows,forest):
    viz = True
    for i in range(row+1,rows):
        if forest[row][col] <= forest[i][col]:
            viz = False
            return viz
    return viz


def look_row_left(row,col,cols,forest):
    viz = True
    for i in range(0,col):
        if forest[row][col] <= forest[row][i]:
            viz = False
            return viz
    return viz


def look_row_right(row,col,cols,forest):
    viz = True
    for i in range(col+1, cols):
        if forest[row][col] <= forest[row][i]:
            viz = False
            return viz
    return viz


def calc_ext(forest):
    tb = len(forest)*2
    lr = (len(forest[0])-2)*2
    total = tb+lr
    return total


def main():
    forest = read_input('sample.txt')
    int_viz = find_viz(forest)
    ext_viz = calc_ext(forest)
    print(f"Interior: {int_viz} Exterior: {ext_viz}  Total: {int_viz+ext_viz}")


if __name__ == "__main__":
    main()