def elf_max_cal(d):
    d_key = 0
    max_cal = 0
    for k in d.keys():
        if d[k] > max_cal:
            d_key = k
            max_cal = d[k]
    return (d_key, max_cal)

def get_cals_top_3(d):
    all_cals = []
    for k in d.keys():
        all_cals.append(d[k])
        all_cals.sort(reverse=True)

    top_3_cals = sum(all_cals[0:3])
    return top_3_cals

with open('/Users/hamish.macdonald/Dev/pyaoc/2022/puzzle_input/day1/input_1.txt', 'r') as input_f:
    input_lines = input_f.readlines()
    elf_cals = {}
    elf_no = 1
    cal_ct = 0
    for l in input_lines[:]:
        if len(l.strip()) > 0:
            cal_ct += int(l.strip())
        else:
            elf_cals[elf_no] = cal_ct
            elf_no += 1
            cal_ct = 0

# add the last elf
elf_cals[elf_no] = cal_ct

print(f'Answer to part 1: {elf_max_cal(elf_cals)}')
print(f'Answer to part 2: {get_cals_top_3(elf_cals)}')