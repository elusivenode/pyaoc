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

def update_validity(d):
    d['is_valid'] = False

def test_data_validity(passport):
    data_is_valid = valid_year(passport['byr'], 1920, 2002)
    if not data_is_valid:
        update_validity(passport)
        return
    data_is_valid = valid_year(passport['iyr'], 2010, 2020)
    if not data_is_valid:
        update_validity(passport)
        return
    data_is_valid = valid_year(passport['eyr'], 2020, 2030)
    if not data_is_valid:
        update_validity(passport)
        return
    data_is_valid = valid_height(passport['hgt'])
    if not data_is_valid:
        update_validity(passport)
        return
    data_is_valid = valid_eye_colour(passport['ecl'])
    if not data_is_valid:
        update_validity(passport)
        return
    data_is_valid = valid_pid(passport['pid'])
    if not data_is_valid:
        update_validity(passport)
        return
    data_is_valid = valid_hair_colour(passport['hcl'])
    if not data_is_valid:
        update_validity(passport)
        return

def valid_char(chars):
    valid = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
    for c in chars:
        if c not in valid:
            return False
    return True

def valid_hair_colour(hc):
    if len(hc) != 7:
        return False
    elif hc[0] != '#':
        return False
    elif not valid_char(hc[1:]):
        return False
    else:
        return True

def valid_pid(p):
    if p.isnumeric() and len(p) == 9:
        return True
    else:
        return False
def valid_year(y, min_y, max_y):
    if y.isnumeric() and int(y) >= min_y and int(y) <= max_y:
        return True
    else:
        return False

def valid_height(h):
    if not ('cm' in h or 'in' in h):
        return False
    elif h.replace('cm','') != h:
        if int(h.replace('cm','')) >= 150 and int(h.replace('cm','')) <= 193:
            return True
        else:
            return False
    else: #should in inches
        if int(h.replace('in','')) >= 59 and int(h.replace('in','')) <= 76:
            return True
        else:
            return False

def valid_eye_colour(c):
    valid = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if c in valid:
        return True
    else:
        return False

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
    if passports[k]['is_valid']:
        test_data_validity(passports[k])

valid_passport_ct = 0
for k in passports:
    if passports[k]['is_valid']:
        valid_passport_ct += 1

print(f'The answer to part 1 is: {valid_passport_ct}')