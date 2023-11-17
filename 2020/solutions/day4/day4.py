def process_passport(record, d):
    data = record.split(' ')
    key_ct = len(d)
    d[key_ct + 1] = {}

    for kv in data:
        k,v = tuple(kv.split(':'))
        d[key_ct + 1][k] = v

def set_passport_validity(d):
    needed = {'pid', 'ecl', 'eyr', 'byr', 'hgt', 'iyr', 'hcl'}
    i = needed.intersection(set(d.keys()))
    if needed == i:
        d['is_valid'] = True
    else:
        d['is_valid'] = False

with open('/Users/hamish.macdonald/Dev/pyaoc/2020/puzzle_input/day4/input_4.txt', 'r') as input_f:
    input_lines = input_f.readlines()
    input_lines.append('')

batch_file = []
record = ''
for l in input_lines[:]:
    l = l.strip()
    if len(l) > 0:
        record += ' ' + l
    else:
        batch_file.append(record.strip())
        record = ''

passports = {}
for r in batch_file:
    process_passport(r,passports)

for k in passports:
    set_passport_validity(passports[k])

valid_passport_ct = 0
for k in passports:
    if passports[k]['is_valid']:
        valid_passport_ct += 1

print(f'The answer to part 1 is: {valid_passport_ct}')