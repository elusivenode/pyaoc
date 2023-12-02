

def find_number(line, words, is_backwards):
    words_s = set(words)
    if is_backwards:
        line = line[::-1]
    for i in range(len(line)):
        line_rem = line[i:]
        if line_rem[0].isdigit():
            return line_rem[0]
        for j in range(len(line_rem)):
            build_number = ''
            for k in range(j+1):
                build_number = build_number + line_rem[k]
                if build_number in words_s:
                    return build_number
    return 'did not find a number'

def calc_ans_2(d):
    a = 0
    for k in d:
        a += int(d[k][0] + d[k][1])
    return a

with open('/Users/hamish.macdonald/Dev/pyaoc/2023/puzzle_input/day1.txt', 'r') as input_f:
#with open('/Users/hamish.macdonald/Dev/pyaoc/2023/puzzle_input/day1_2_test.txt', 'r') as input_f:
    input_lines = input_f.readlines()

calibration_document = []
for l in input_lines[:]:
    calibration_document.append(l.strip())

word_numbers = ['one','two','three','four','five','six','seven','eight','nine']
word_numbers_b = []
for w in word_numbers:
    word_numbers_b.append(w[::-1])

document_numbers = {}
for line in calibration_document:
    document_numbers[line] = []
    f = find_number(line, word_numbers, False)
    l = find_number(line, word_numbers_b,  True)
    if f.isdigit():
        document_numbers[line].insert(0,f)
    else:
        document_numbers[line].insert(0, str(word_numbers.index(f)+1))
    if l.isdigit():
        document_numbers[line].append(l)
    else:
        document_numbers[line].append(str(word_numbers_b.index(l)+1))

print(f'The answer to part 2 is {calc_ans_2(document_numbers)}.')
