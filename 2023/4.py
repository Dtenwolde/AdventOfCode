import re
input_ = open("4_input.txt").read().split("\n")
sum_ = 0

for line in input_:
    card, numbers = line.split(":")
    winning_numbers, my_numbers = numbers.split("|")
    winning_numbers = set([int(i) for i in winning_numbers.split()])
    my_numbers = ([int(i) for i in my_numbers.split()])
    numbers_won_length = len(winning_numbers.intersection(my_numbers))
    if numbers_won_length >= 1:
        won = 1
        for _ in range(1, numbers_won_length):
            won *= 2
        sum_ += won

print(sum_)

max_number_of_cards = 0
total_runs = [0 for _ in range(len(input_))]

for idx, line in enumerate(input_):
    total_runs[idx] += 1
    card, numbers = line.split(":")
    card_number = int(card.split()[-1])
    winning_numbers, my_numbers = numbers.split("|")
    winning_numbers = set([int(i) for i in winning_numbers.split()])
    my_numbers = ([int(i) for i in my_numbers.split()])
    numbers_won_length = len(winning_numbers.intersection(my_numbers))
    if numbers_won_length > 0:
        max_number_of_cards += 2**(numbers_won_length-1)
    for j in range(numbers_won_length):
        total_runs[idx+j+1] += total_runs[idx]
print(max_number_of_cards)
print(sum(total_runs))


# 1 2 4 8 14 1