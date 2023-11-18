def count_affirmative_answers(d, k):
     d[k]['distinct_ct'] = len(set(d[k]['answers']))

def get_total_sum_affirmative(d):
    total = 0
    for k in d:
        total += d[k]['distinct_ct']
    return total

with open('/Users/hamish.macdonald/Dev/pyaoc/2020/puzzle_input/day6/input_6.txt', 'r') as input_f:
    input_lines = input_f.readlines()
    input_lines.append('')

group_answers = []
record = ''
for l in input_lines[:]:
    l = l.strip()
    if len(l) > 0:
        record += l
    else:
        group_answers.append(record.strip())
        record = ''

group_no = 1
group_answer_counts = {}
for a in group_answers:
    group_answer_counts[group_no] = {'answers':a}
    count_affirmative_answers(group_answer_counts, group_no)
    group_no += 1

print(f'The answer to part 1 in {get_total_sum_affirmative(group_answer_counts)}')