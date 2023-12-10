def endswithz(l):
    for e in l:
        if not e.endswith("Z"):
            return False
    return True




def main():
    input_ = open("8_input.txt").read().split("\n")
    instructions = input_[0]
    graph_ = input_[2:]
    final_graph = {}
    for conn in graph_:
        node, edge = conn.split("=")
        edge = edge.replace("(", "").replace(")", "").replace(" ", "").strip()
        edges = edge.split(",")
        final_graph[node.strip()] = (edges[0], edges[1])
    positions = [pos for pos in final_graph.keys() if pos.endswith("A")]
    counter_per_pos = []

    def map_execute(pos):
        instruction_counter = 0
        while not pos.endswith("Z"):
            for instruction in instructions:
                instruction_counter += 1
                if instruction == "L":
                    next_pos = final_graph[pos][0]
                else:
                    next_pos = final_graph[pos][1]
                if endswithz(next_pos):
                    return instruction_counter
                pos = next_pos
                print(pos, next_pos)
        return instruction_counter
    for pos in positions:
        counter_per_pos.append(map_execute(pos))

    from math import lcm
    print(f"Part 2: {lcm(*counter_per_pos)}")
if __name__ == "__main__":
    print(main())
