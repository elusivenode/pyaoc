def find_numbers(schematic, nums):
    nums_dict = {}
    for i,r in enumerate(nums):
        num = ''
        prev_flag = ''
        start_idx = ''
        looking_for_start_idx = True
        for j,c in enumerate(r):
            if c == 1:
                curr_char = schematic[i][j]
                num += curr_char
                if looking_for_start_idx:
                    start_idx = j
                    looking_for_start_idx = False
            if c == 0 and prev_flag == 1:
                nums_dict[num] = {}
                nums_dict[num]['row'] = i
                nums_dict[num]['start_idx'] = start_idx
                nums_dict[num]['end_idx'] = j - 1
                num = ''
                looking_for_start_idx = True
            prev_flag = c
    return nums_dict

#with open('/Users/hamish.macdonald/Dev/pyaoc/2023/puzzle_input/day2.txt', 'r') as input_f:
with open('/Users/hamish.macdonald/Dev/pyaoc/2023/puzzle_input/day3_1_test.txt', 'r') as input_f:
    input_lines = input_f.readlines()

schematic = []
for l in input_lines[:]:
    schematic.append(list(l.strip()))

numbers = []
symbols = []
for i, row in enumerate(schematic):
    numbers.append([])
    symbols.append([])
    for j, num in enumerate(row):
        if num.isdigit():
            numbers[i].append(1)
        else:
            numbers[i].append(0)
        if not (num.isdigit() or num == '.'):
            symbols[i].append(1)
        else:
            symbols[i].append(0)

a = find_numbers(schematic, numbers)
print(a)
