import re
input_ = open("1_input.txt").read().split("\n")

# sum = 0
# for line in input_:
#     line = re.sub("[^0-9]", "", line)
#     first = line[0]
#     last = line[-1]
#     sum += int(first+last)
# print(sum)

digits = [('one', 'one1one'), ('two', 'two2two'), ('three', 'three3three'),
          ('four', 'four4four'), ('five', 'five5five'), ('six', 'six6six'),
          ('seven', 'seven7seven'), ('eight', 'eight8eight'), ('nine', 'nine9nine')]
sum2 = 0
for line in input_:
    for digit in digits:
        line = line.replace(digit[0], digit[1])
        print(line)
    print(line)
    line = re.sub("[^0-9]", "", line)
    first = line[0]
    last = line[-1]
    print(first + last)
    sum2 += int(first+last)
print(sum2)
