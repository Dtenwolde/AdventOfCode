import re
input_ = open("2_input.txt").read().split("\n")

sum_game_id = 0
for line in input_:
    min_red = 0
    min_green = 0
    min_blue = 0
    game_id, games = line.split(":")
    game_identifier = int(game_id.split()[-1])
    individual_games = games.split(";")
    for game in individual_games:
        cubes = game.split(",")
        for cube in cubes:
            split_cube = cube.split()
            if split_cube[-1] == "red":
                min_red = max(min_red, int(split_cube[0]))
            elif split_cube[-1] == "green":
                min_green = max(min_green, int(split_cube[0]))
            elif split_cube[-1] == "blue":
                min_blue = max(min_blue, int(split_cube[0]))
    sum_game_id += (min_red*min_green*min_blue)
print(sum_game_id)