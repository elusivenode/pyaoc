def password_is_valid(min, max, ltr, password):
    occurrences = password.count(ltr)
    if occurrences >= min and occurrences <= max:
        return True
    else:
        return False

def password_is_valid_2(min, max, ltr, password):
    if (password[min-1] + password[max-1]).count(ltr) == 1:
        return True
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
password_validity_2 = {True: set(), False: set()}
for min_ct, max_ct, letter, password in passwords:
    is_valid = password_is_valid(min_ct, max_ct, letter, password)
    is_valid_2 = password_is_valid_2(min_ct, max_ct, letter, password)
    if is_valid:
        password_validity[True].add((min_ct, max_ct, letter, password))
    else:
        password_validity[False].add((min_ct, max_ct, letter, password))
    if is_valid_2:
        password_validity_2[True].add((min_ct, max_ct, letter, password))
    else:
        password_validity_2[False].add((min_ct, max_ct, letter, password))


print(f'Answer to part 1: {len(password_validity[True])}')
print(f'Answer to part 2: {len(password_validity_2[True])}')
