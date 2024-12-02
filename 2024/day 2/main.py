def is_safe(values):
    """Check if the levels are all increasing or decreasing and differences are within [1, 3]."""
    increasing = all(values[i] < values[i + 1] for i in range(len(values) - 1))
    decreasing = all(values[i] > values[i + 1] for i in range(len(values) - 1))
    valid_differences = all(1 <= abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1))
    return (increasing or decreasing) and valid_differences


def part2():
    result = 0
    with open('input.txt') as file:
        for line in file:
            values = [int(i) for i in line.split()]

            # Check if the report is safe without any modification
            if is_safe(values):
                result += 1
                continue

            # Check if the report becomes safe by removing one level
            safe_with_removal = False
            for i in range(len(values)):
                modified_values = values[:i] + values[i + 1:]  # Remove the ith level
                if is_safe(modified_values):
                    safe_with_removal = True
                    break

            if safe_with_removal:
                result += 1

    print(result)
def part1():
    result = 0
    with open('input.txt') as file:
        for level in file:
            values = [int(i) for i in level.split()]
            increasing = values[0] < values[1]
            safe = True
            idx = 1
            while safe and idx < len(values):
                diff = abs(values[idx-1] - values[idx])
                if diff > 3:
                    safe = False
                    print(f"{diff=}")
                if increasing and values[idx-1] > values[idx]:
                    safe = False
                    print(values[idx-1], values[idx], increasing)
                if values[idx-1] == values[idx]:
                    safe = False
                if not increasing and values[idx-1] < values[idx]:
                    safe = False
                    print(values[idx - 1], values[idx], increasing)
                idx += 1
            print(f"{values=}, {safe=}, {increasing=}")
            if safe:
                result += 1
    print(result)

if __name__ == "__main__":
    # part1()
    part2()