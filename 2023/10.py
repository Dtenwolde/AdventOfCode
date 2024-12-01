from collections import defaultdict

class Coordinate:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    __repr__ = __str__

def part1():
    input_ = open("10_input.txt").read().split("\n")
    edges = []
    next_pos = []
    graph_dict = {}
    for idx_y, line in enumerate(input_):
        for idx_x, point in enumerate(line):
            if point == "|":
                edges.append(((idx_y-1, idx_x), (idx_y, idx_x)))
                edges.append(((idx_y+1, idx_x), (idx_y, idx_x)))

                # edges.append(((idx_y, idx_x), (idx_y-1, idx_x)))
                # edges.append(((idx_y, idx_x), (idx_y+1, idx_x)))
            elif point == "-":
                edges.append(((idx_y, idx_x-1), (idx_y, idx_x)))
                edges.append(((idx_y, idx_x+1), (idx_y, idx_x)))

                # edges.append(((idx_y, idx_x), (idx_y, idx_x-1)))
                # edges.append(((idx_y, idx_x), (idx_y, idx_x+1)))
            elif point == "L":
                edges.append(((idx_y - 1, idx_x), (idx_y, idx_x)))
                edges.append(((idx_y, idx_x+1), (idx_y, idx_x)))

                # edges.append(((idx_y, idx_x), (idx_y - 1, idx_x)))
                # edges.append(((idx_y, idx_x), (idx_y, idx_x + 1)))
            elif point == "J":
                edges.append(((idx_y - 1, idx_x), (idx_y, idx_x)))
                edges.append(((idx_y, idx_x - 1), (idx_y, idx_x)))

                # edges.append(((idx_y, idx_x), (idx_y - 1, idx_x)))
                # edges.append(((idx_y, idx_x), (idx_y, idx_x - 1)))
            elif point == "7":
                edges.append(((idx_y + 1, idx_x), (idx_y, idx_x)))
                edges.append(((idx_y, idx_x - 1), (idx_y, idx_x)))

                # edges.append(((idx_y, idx_x), (idx_y + 1, idx_x)))
                # edges.append(((idx_y, idx_x), (idx_y, idx_x - 1)))
            elif point == "F":
                edges.append(((idx_y + 1, idx_x), (idx_y, idx_x)))
                edges.append(((idx_y, idx_x + 1), (idx_y, idx_x)))

                # edges.append(((idx_y, idx_x), (idx_y + 1, idx_x)))
                # edges.append(((idx_y, idx_x), (idx_y, idx_x + 1)))
            elif point == "S":
                next_pos.append(((idx_y, idx_x), 0))
    for edge in edges:
        if edge[0] in graph_dict:
            graph_dict[edge[0]].append(edge[1])
        else:
            graph_dict[edge[0]] = [edge[1]]
    print(graph_dict)
    seen = {}
    while len(next_pos) > 0:
        current_pos, distance = next_pos.pop(0)
        if current_pos in seen:
            continue
        seen[current_pos] = distance
        if current_pos  in graph_dict:
            for v in graph_dict[current_pos]:
                next_pos.append((v, distance + 1))

    print(seen)
    print(max(seen.values()))
def part2():
    input_ = open("10_input.txt").read().split("\n")



if __name__ == "__main__":
    part1()
    part2()