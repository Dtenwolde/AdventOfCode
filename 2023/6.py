input_ = open("6_input.txt").read().split("\n")

# time = list(map(int,input_[0].split(":")[-1].split()))
# distance = list(map(int,input_[1].split(":")[-1].split()))
#
# races = zip(time, distance)
# total_win = 1
# for race in races:
#     winning = 0
#     total_time, to_beat = race
#     for i in range(total_time):
#         distance = (total_time - i) * i
#         if distance > to_beat:
#             winning += 1
#     total_win *= winning
# print(total_win)

total_time = int(input_[0].split(":")[-1].replace(" ", ""))
to_beat = int(input_[1].split(":")[-1].replace(" ", ""))

winning = 0
for i in range(total_time):
    distance = (total_time - i) * i
    if distance > to_beat:
        winning += 1

print(winning)

