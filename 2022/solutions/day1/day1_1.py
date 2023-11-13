def elf_max_cal(d):
    d_key = 0
    max_cal = 0
    for k in d.keys():
        if d[k] > max_cal:
            d_key = k
            max_cal = d[k]
    return (d_key, max_cal)

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

print(elf_max_cal(elf_cals))