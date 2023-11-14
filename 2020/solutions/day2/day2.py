def password_is_valid(min, max, ltr, password):
    occurrences = password.count(ltr)
    if occurrences >= min and occurrences <= max:
        return True
    else:
        return False


with open('/Users/hamish.macdonald/Dev/pyaoc/2020/puzzle_input/day2/input_2.txt', 'r') as input_f:
    input_lines = input_f.readlines()

passwords = []
for l in input_lines[:]:
    a,b = l.split(':')
    c,letter = a.split(' ')
    min_ct, max_ct = c.split('-')
    password = b.strip()
    passwords.append((int(min_ct),int(max_ct),letter,password))

password_validity = {True: set(), False: set()}
for min_ct, max_ct, letter, password in passwords:
    is_valid = password_is_valid(min_ct, max_ct, letter, password)
    if is_valid:
        password_validity[True].add((min_ct, max_ct, letter, password))
    else:
        password_validity[False].add((min_ct, max_ct, letter, password))

print(f'Answer to part 1: {len(password_validity[True])}')