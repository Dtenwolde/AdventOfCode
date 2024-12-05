

def part2():
    input_data = open("input.txt").readlines()
    word_matrix = [list(line.strip()) for line in input_data]
    result = 0

    # Get dimensions of the matrix
    rows = len(word_matrix)
    cols = len(word_matrix[0])

    # Iterate over the matrix
    for y_idx in range(1, rows - 1):  # Start at 1 and end at rows - 1 to avoid out-of-bounds
        for x_idx in range(1, cols - 1):  # Same for columns
            # Check if the current position contains "A"
            if word_matrix[y_idx][x_idx] != "A":
                continue
            print(f"{y_idx=}, {x_idx=}")


                # Orientation 5: M on diagonals (bottom-left and top-left), S on diagonals (top-right and bottom-right)
            if (
                    word_matrix[y_idx + 1][x_idx - 1] == "M" and  # Bottom-left "M"
                    word_matrix[y_idx - 1][x_idx - 1] == "M" and  # Top-left "M"
                    word_matrix[y_idx - 1][x_idx + 1] == "S" and  # Top-right "S"
                    word_matrix[y_idx + 1][x_idx + 1] == "S"  # Bottom-right "S"
            ):
                result += 1

                # Orientation 6: S on diagonals (bottom-left and top-left), M on diagonals (top-right and bottom-right)
            if (
                    word_matrix[y_idx + 1][x_idx - 1] == "S" and  # Bottom-left "S"
                    word_matrix[y_idx - 1][x_idx - 1] == "S" and  # Top-left "S"
                    word_matrix[y_idx - 1][x_idx + 1] == "M" and  # Top-right "M"
                    word_matrix[y_idx + 1][x_idx + 1] == "M"  # Bottom-right "M"
            ):
                result += 1


            # Orientation 7: M on top-left and top-right, S on bottom-left and bottom-right
            if (
                word_matrix[y_idx - 1][x_idx - 1] == "M" and  # Top-left "M"
                word_matrix[y_idx - 1][x_idx + 1] == "M" and  # Top-right "M"
                word_matrix[y_idx + 1][x_idx - 1] == "S" and  # Bottom-left "S"
                word_matrix[y_idx + 1][x_idx + 1] == "S"      # Bottom-right "S"
            ):
                result += 1

            # Orientation 8: S on top-left and top-right, M on bottom-left and bottom-right
            if (
                word_matrix[y_idx - 1][x_idx - 1] == "S" and  # Top-left "S"
                word_matrix[y_idx - 1][x_idx + 1] == "S" and  # Top-right "S"
                word_matrix[y_idx + 1][x_idx - 1] == "M" and  # Bottom-left "M"
                word_matrix[y_idx + 1][x_idx + 1] == "M"      # Bottom-right "M"
            ):
                result += 1
    print(result)

def find_right(word_matrix, x_idx, y_idx):
    try:
        if word_matrix[x_idx][y_idx + 1] != "M":
            return False
        if word_matrix[x_idx][y_idx + 2] != "A":
            return False
        if word_matrix[x_idx][y_idx + 3] != "S":
            return False
    except IndexError:
        return False
    print(f"Found right {x_idx=}, {y_idx=}")
    return True


def find_left(word_matrix, x_idx, y_idx):
    if y_idx - 3 < 0:
        return False
    try:
        if word_matrix[x_idx][y_idx - 1] != "M":
            return False
        if word_matrix[x_idx][y_idx - 2] != "A":
            return False
        if word_matrix[x_idx][y_idx - 3] != "S":
            return False
    except IndexError:
        return False
    print(f"Found left {x_idx=}, {y_idx=}")
    return True


def find_down(word_matrix, x_idx, y_idx):
    try:
        if word_matrix[x_idx + 1][y_idx] != "M":
            return False
        if word_matrix[x_idx + 2][y_idx] != "A":
            return False
        if word_matrix[x_idx + 3][y_idx] != "S":
            return False
    except IndexError:
        return False
    print(f"Found down {x_idx=}, {y_idx=}")
    return True


def find_up(word_matrix, x_idx, y_idx):
    if x_idx - 3 < 0:
        return False
    try:
        if word_matrix[x_idx - 1][y_idx] != "M":
            return False
        if word_matrix[x_idx - 2][y_idx] != "A":
            return False
        if word_matrix[x_idx - 3][y_idx] != "S":
            return False
    except IndexError:
        return False
    print(f"Found up {x_idx=}, {y_idx=}")
    return True


def find_down_right(word_matrix, x_idx, y_idx):
    try:
        if word_matrix[x_idx + 1][y_idx + 1] != "M":
            return False
        if word_matrix[x_idx + 2][y_idx + 2] != "A":
            return False
        if word_matrix[x_idx + 3][y_idx + 3] != "S":
            return False
    except IndexError:
        return False
    print(f"Found down-right {x_idx=}, {y_idx=}")
    return True


def find_down_left(word_matrix, x_idx, y_idx):
    if y_idx - 3 < 0:
        return False
    try:
        if word_matrix[x_idx + 1][y_idx - 1] != "M":
            return False
        if word_matrix[x_idx + 2][y_idx - 2] != "A":
            return False
        if word_matrix[x_idx + 3][y_idx - 3] != "S":
            return False
    except IndexError:
        return False
    print(f"Found down-left {x_idx=}, {y_idx=}")
    return True


def find_up_right(word_matrix, x_idx, y_idx):
    if x_idx - 3 < 0:
        return False
    try:
        if word_matrix[x_idx - 1][y_idx + 1] != "M":
            return False
        if word_matrix[x_idx - 2][y_idx + 2] != "A":
            return False
        if word_matrix[x_idx - 3][y_idx + 3] != "S":
            return False
    except IndexError:
        return False
    print(f"Found up-right {x_idx=}, {y_idx=}")
    return True


def find_up_left(word_matrix, x_idx, y_idx):
    if x_idx - 3 < 0 or y_idx - 3 < 0:
        return False
    try:
        if word_matrix[x_idx - 1][y_idx - 1] != "M":
            return False
        if word_matrix[x_idx - 2][y_idx - 2] != "A":
            return False
        if word_matrix[x_idx - 3][y_idx - 3] != "S":
            return False
    except IndexError:
        return False
    print(f"Found up-left {x_idx=}, {y_idx=}")
    return True

def part1():
    input_data = open("input.txt").readlines()
    word_matrix = [list(line.strip()) for line in input_data]
    result = 0
    counted_positions = set()  # To keep track of already counted words

    for x_idx in range(len(word_matrix)):
        for y_idx in range(len(word_matrix[0])):
            print(f"{x_idx=}, {y_idx=}")
            if word_matrix[x_idx][y_idx] != "X":
                continue

            # Check all directions
            if find_right(word_matrix, x_idx, y_idx) and (x_idx, y_idx, "right") not in counted_positions:
                result += 1
                counted_positions.add((x_idx, y_idx, "right"))

            if find_left(word_matrix, x_idx, y_idx) and (x_idx, y_idx, "left") not in counted_positions:
                result += 1
                counted_positions.add((x_idx, y_idx, "left"))

            if find_down(word_matrix, x_idx, y_idx) and (x_idx, y_idx, "down") not in counted_positions:
                result += 1
                counted_positions.add((x_idx, y_idx, "down"))

            if find_up(word_matrix, x_idx, y_idx) and (x_idx, y_idx, "up") not in counted_positions:
                result += 1
                counted_positions.add((x_idx, y_idx, "up"))

            if find_down_right(word_matrix, x_idx, y_idx) and (x_idx, y_idx, "down_right") not in counted_positions:
                result += 1
                counted_positions.add((x_idx, y_idx, "down_right"))

            if find_down_left(word_matrix, x_idx, y_idx) and (x_idx, y_idx, "down_left") not in counted_positions:
                result += 1
                counted_positions.add((x_idx, y_idx, "down_left"))

            if find_up_right(word_matrix, x_idx, y_idx) and (x_idx, y_idx, "up_right") not in counted_positions:
                result += 1
                counted_positions.add((x_idx, y_idx, "up_right"))

            if find_up_left(word_matrix, x_idx, y_idx) and (x_idx, y_idx, "up_left") not in counted_positions:
                result += 1
                counted_positions.add((x_idx, y_idx, "up_left"))

    print(result)

if __name__ == "__main__":
    # part1()
    part2()