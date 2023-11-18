

with open('/Users/hamish.macdonald/Dev/pyaoc/2020/puzzle_input/day6/input_6.txt', 'r') as input_f:
    input_lines = input_f.readlines()

group_no = 1
member_no = 1
groups = [group_no]
answers = {}
answers[group_no] = {}

for l in input_lines:
    if len(l.strip()) == 0:
        group_no += 1
        groups.append(group_no)
        answers[group_no] = {}
        member_no = 1
        continue
    answers[group_no][member_no] = l.strip()
    member_no += 1

group_common_answers = {}
for g in groups:
    exec_str = 'set.intersection('
    for m in answers[g]:
        exec(f'set_{m} = set()')
        for a in answers[g][m]:
            exec(f'set_{m}.add("{a}")')
        exec_str += f'set_{m},'
    exec_str = exec_str[:-1]
    exec_str += ')'
    exec(f'common_answers = {exec_str}')
    group_common_answers[g] = len(common_answers)

total = 0
for k in group_common_answers:
    total += group_common_answers[k]

print(f'The answer to part 2 is {total}')