def get_row(bp):
    rng = [0,127]
    for e in bp:
        if e == 'F':
            rng[1] = (rng[0] + rng[1] - 1) / 2
        else:
            rng[0] = (rng[0] + rng[1] + 1) / 2
    return int(rng[0])

def get_col(bp):
    rng = [0,8]
    for e in bp:
        if e == 'L':
            rng[1] = (rng[0] + rng[1] - 1) / 2
        else:
            rng[0] = (rng[0] + rng[1] + 1) / 2
    return int(rng[0])

def get_max_seat_id(d):
    m = 0
    for s in d:
        if d[s]['seat_id'] > m:
            m = d[s]['seat_id']
    return m

with open('/Users/hamish.macdonald/Dev/pyaoc/2020/puzzle_input/day5/input_5.txt', 'r') as input_f:
    input_lines = input_f.readlines()

boarding_passes = []
for l in input_lines[:]:
    boarding_passes.append(l.strip())

bp_seat_nos = {}
for bp in boarding_passes:
    row = get_row(bp[:7])
    col = get_col(bp[7:])
    bp_seat_nos[bp] = {}
    bp_seat_nos[bp][row] = row
    bp_seat_nos[bp][col] = col
    bp_seat_nos[bp]['seat_id'] = row * 8 + col

print(f'The answer to part 1 is {get_max_seat_id(bp_seat_nos)}')