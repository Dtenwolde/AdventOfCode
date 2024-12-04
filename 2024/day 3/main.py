import re

def part2():
    result = 0
    with open('input.txt') as file:
        input = file.read()
        enabled = True
        all_cases = re.finditer("mul\([0-9]+,[0-9]+\)", input)
        control_cases = re.finditer("((do)|(don't))(\(\))", input)

        # Collect matches with their spans and a label for their type
        matches = []

        # Add all_cases matches
        for match in all_cases:
            matches.append((match.span()[0], match.span()[1], "mul", match.group()))

        # Add control_cases matches
        for match in control_cases:
            matches.append((match.span()[0], match.span()[1], "control", match.group()))

        # Sort matches by their starting index
        matches.sort(key=lambda x: x[0])

        for start, end, match_type, text in matches:
            if match_type == "control":
                enabled = text == "do()"
            else:
                if not enabled:
                    continue
                else:
                    numbers = text[4:-1].split(",")
                    result += int(numbers[0]) * int(numbers[1])
    print(result)
def part1():
    result = 0
    with open('input.txt') as file:
        input = file.read()
        all_cases = re.findall("mul\([0-9]+,[0-9]+\)", input)
        for case in all_cases:
            numbers = case[4:-1].split(",")
            result += int(numbers[0]) * int(numbers[1])

    print(result)
if __name__ == "__main__":
    # part1()
    part2()