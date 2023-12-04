import re
input_ = open("3_input.txt").read().split("\n")
#
# sum = 0
# char_coords = []
# digits_found = []
# for y, line in enumerate(input_):
#     current_digit = ""
#     start_idx = (-1,-1)
#     for x, char in enumerate(line):
#         if not char.isdigit() and char != ".":
#             char_coords.append((x,y))
#             if current_digit != "": # Currently working on a digit, can now be added to list and reset
#                 digits_found.append((current_digit, start_idx))
#                 current_digit = ""
#                 start_idx = (-1, -1)
#         elif char.isdigit(): # initialize starting position and register digit
#             if start_idx == (-1,-1):
#                 start_idx = (x,y)
#             current_digit += char
#         else: # found a period (.), add digit to list and reset
#             if current_digit != "":
#                 digits_found.append((current_digit, start_idx))
#                 current_digit = ""
#                 start_idx = (-1, -1)
#     if current_digit != "": # We are at the end of a line but found a digit on the last iteration
#         digits_found.append((current_digit, start_idx))
#
# print(digits_found)
# print(char_coords)
# print(input_)
#
# for digit, (start_x, start_y) in digits_found:
#     for x in range(start_x, start_x + len(digit)):
#         if (x-1, start_y-1) in char_coords:
#             sum += int(digit)
#             break
#         elif (x-1, start_y) in char_coords:
#             sum += int(digit)
#             break
#         elif (x-1, start_y+1) in char_coords:
#             sum += int(digit)
#             break
#         elif (x, start_y-1) in char_coords:
#             sum += int(digit)
#             break
#         elif (x, start_y+1) in char_coords:
#             sum += int(digit)
#             break
#         elif (x+1, start_y-1) in char_coords:
#             sum += int(digit)
#             break
#         elif (x+1, start_y ) in char_coords:
#             sum += int(digit)
#             break
#         elif (x+1, start_y+1) in char_coords:
#             sum += int(digit)
#             break
#
# print(sum)

## part 2
sum = 0
char_coords = {}
digits_found = []
for y, line in enumerate(input_):
    current_digit = ""
    start_idx = (-1,-1)
    for x, char in enumerate(line):
        if not char.isdigit() and char == "*":
            char_coords[(x,y)] = []
            if current_digit != "": # Currently working on a digit, can now be added to list and reset
                digits_found.append((current_digit, start_idx))
                current_digit = ""
                start_idx = (-1, -1)
        elif char.isdigit(): # initialize starting position and register digit
            if start_idx == (-1,-1):
                start_idx = (x,y)
            current_digit += char
        else: # found a period (.), add digit to list and reset
            if current_digit != "":
                digits_found.append((current_digit, start_idx))
                current_digit = ""
                start_idx = (-1, -1)
    if current_digit != "": # We are at the end of a line but found a digit on the last iteration
        digits_found.append((current_digit, start_idx))

for digit, (start_x, start_y) in digits_found:
    for x in range(start_x, start_x + len(digit)):
        if (x-1, start_y-1) in char_coords:
            char_coords[x-1, start_y-1].append(digit)
            break
        elif (x-1, start_y) in char_coords:
            char_coords[x-1, start_y].append(digit)
            break
        elif (x-1, start_y+1) in char_coords:
            char_coords[x-1, start_y+1].append(digit)
            break
        elif (x, start_y-1) in char_coords:
            char_coords[x, start_y-1].append(digit)
            break
        elif (x, start_y+1) in char_coords:
            char_coords[x, start_y+1].append(digit)
            break
        elif (x+1, start_y-1) in char_coords:
            char_coords[x+1, start_y-1].append(digit)
            break
        elif (x+1, start_y ) in char_coords:
            char_coords[x+1, start_y].append(digit)
            break
        elif (x+1, start_y+1) in char_coords:
            char_coords[x+1, start_y+1].append(digit)
            break

for key, value in char_coords.items():
    if len(value) == 2:
        sum += int(value[0]) * int(value[1])

print(sum)




#
#
# for x,y in char_coords:
#     try:
#         if input_[y-1][x-1].isdigit():
#             digits_found.append((x-1, y-1))
#         if input_[y-1][x].isdigit():
#             digits_found.append((x, y-1))
#         if input_[y-1][x+1].isdigit():
#             digits_found.append((x+1, y-1))
#         if input_[y][x-1].isdigit():
#             digits_found.append((x-1, y))
#         if input_[y][x+1].isdigit():
#             digits_found.append((x+1, y))
#         if input_[y+1][x-1].isdigit():
#             digits_found.append((x-1, y+1))
#         if input_[y+1][x].isdigit():
#             digits_found.append((x, y+1))
#         if input_[y+1][x+1].isdigit():
#             digits_found.append((x+1, y+1))
#     except:
#         continue
# print(input_)
# print(digits_found)
#
# for digit in digits_found:
#