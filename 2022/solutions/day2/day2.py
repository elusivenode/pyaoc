
def game_result(game, win_map):
    return win_map[game]

def score_game(res, choice):
    res_pts = score_map[res]
    choice_pts = our_choice_map[choice]
    return (res_pts, choice_pts)

with open('/Users/hamish.macdonald/Dev/pyaoc/2022/puzzle_input/day2/input_2.txt', 'r') as input_f:
    input_lines = input_f.readlines()

games = []
for l in input_lines:
    ls = l.strip()
    games.append(tuple(ls.split(' ')))

win_map = {}
win_map[('A','X')] = 'D'
win_map[('A','Y')] = 'W'
win_map[('A','Z')] = 'L'
win_map[('B','X')] = 'L'
win_map[('B','Y')] = 'D'
win_map[('B','Z')] = 'W'
win_map[('C','X')] = 'W'
win_map[('C','Y')] = 'L'
win_map[('C','Z')] = 'D'

score_map = {}
score_map['W'] = 6
score_map['D'] = 3
score_map['L'] = 0

our_choice_map = {}
our_choice_map['X'] = 1
our_choice_map['Y'] = 2
our_choice_map['Z'] = 3

total_pts = 0
for g in games:
    res = game_result(g,win_map)
    choice = g[1]
    res_pts, choice_pts = score_game(res,choice)
    total_pts = total_pts + res_pts + choice_pts

print(f"Answer to part 1: {total_pts}")