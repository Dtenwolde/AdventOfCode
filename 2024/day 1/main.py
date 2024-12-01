import duckdb
from collections import defaultdict


def part2():
    input = duckdb.sql("from read_csv_auto('input.txt', sep=' ')").fetchall()
    left_list = [i[0] for i in input]
    right_list = [i[-1] for i in input]
    result_dict = defaultdict(int)
    for i in range(len(right_list)):
        result_dict[right_list[i]] += 1
    result = 0
    for i in range(len(left_list)):
        result += left_list[i] * result_dict[left_list[i]]
    print(result)

def part1():
    input = duckdb.sql("from read_csv_auto('input.txt', sep=' ')").fetchall()
    left_list = sorted([i[0] for i in input])
    right_list = sorted([i[-1] for i in input])
    result = 0
    for i in range(len(left_list)):
        result += abs(left_list[i] - right_list[i])
    print(result)

if __name__ == "__main__":
    part1()
    part2()