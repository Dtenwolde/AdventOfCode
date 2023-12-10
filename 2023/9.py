
def part1():
    input_ = open("9_input.txt").read().split("\n")
    sum = 0
    for line in input_:
        line = list(map(int, line.split()))
        line_history = [line]
        while not all(v == 0 for v in line):
            diff_list = []
            for idx in range(1,len(line)):
                diff_list.append(line[idx] - line[idx-1])
            line_history.append(diff_list)
            line = diff_list
        for idx in range(len(line_history)-1, 0, -1):
            line_history[idx-1].append(line_history[idx-1][-1]+line_history[idx][-1])
        sum += line_history[0][-1]
    print(sum)

def part2():
    input_ = open("9_input.txt").read().split("\n")
    sum = 0
    for line in input_:
        line = list(map(int, line.split()))
        line_history = [line]
        while not all(v == 0 for v in line):
            diff_list = []
            for idx in range(1,len(line)):
                diff_list.append(line[idx] - line[idx-1])
            line_history.append(diff_list)
            line = diff_list
        for idx in range(len(line_history)-1, 0, -1):
            line_history[idx-1].insert(0, (line_history[idx-1][0]-line_history[idx][0]))
        sum += line_history[0][0]
    print(sum)

if __name__ == "__main__":
    part1()
    part2()