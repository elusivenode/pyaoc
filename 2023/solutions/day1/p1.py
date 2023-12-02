
def find_first_int(s):
    if s.isdigit():
        return s

def calc_ans_1(d):
    a = 0
    for k in d:
        a += int(d[k][0] + d[k][1])
    return a

with open('/Users/hamish.macdonald/Dev/pyaoc/2023/puzzle_input/day1.txt', 'r') as input_f:
    input_lines = input_f.readlines()

calibration_document = []
for l in input_lines[:]:
    calibration_document.append(l.strip())

doc_first_last_digits = {}
for doc in calibration_document:
    doc_first_last_digits[doc] = []
    for c in doc:
        if find_first_int(c) is not None:
            doc_first_last_digits[doc].append(c)
            break
    for c in doc[::-1]:
        if find_first_int(c) is not None:
            doc_first_last_digits[doc].append(c)
            break

print(f'The answer to part 1 is {calc_ans_1(doc_first_last_digits)}.')