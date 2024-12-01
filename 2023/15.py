
def part1():
    input_ = open("15_input.txt").read().split(",")
    result = 0
    for hash_string in input_:
        current_value = 0
        for char in hash_string:
            current_value += ord(char)
            current_value *= 17
            current_value = current_value % 256
        result += current_value
    print(result)
def part2():
    input_ = open("10_input.txt").read().split("\n")



if __name__ == "__main__":
    part1()
    part2()