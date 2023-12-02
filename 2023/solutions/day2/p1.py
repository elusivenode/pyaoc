def parse_games(d,g):
    game, colours = g.split(':')
    _, game_no = game.split(' ')
    d[game_no] = {}
    selections = colours.split(';')
    ct = 1
    for s in selections:
        sl = s.split(',')
        d[game_no][ct] = {}
        for i in sl:
            v,k = i.strip().split(' ')
            d[game_no][ct][k] = v
        ct += 1

def is_game_legal(g):
    for gn in g:
        if 'red' in g[gn] and int(g[gn]['red']) > 12:
            return False
        if 'green' in g[gn] and int(g[gn]['green']) > 13:
            return False
        if 'blue' in g[gn] and int(g[gn]['blue']) > 14:
            return False
    return True

def min_rgb_power(g):
    min_r, min_g, min_b = (0,0,0)
    for gn in g:
        if 'red' in g[gn] and int(g[gn]['red']) > min_r:
            min_r = int(g[gn]['red'])
        if 'green' in g[gn] and int(g[gn]['green']) > min_g:
            min_g = int(g[gn]['green'])
        if 'blue' in g[gn] and int(g[gn]['blue']) > min_b:
            min_b = int(g[gn]['blue'])
    return min_r * min_g * min_b

def part_1_answer(d):
    score = 0
    for k in d:
        if d[k]:
            score += int(k)
    return score

with open('/Users/hamish.macdonald/Dev/pyaoc/2023/puzzle_input/day2.txt', 'r') as input_f:
#with open('/Users/hamish.macdonald/Dev/pyaoc/2023/puzzle_input/day2_1_test.txt', 'r') as input_f:
    input_lines = input_f.readlines()

games = {}
for l in input_lines[:]:
    parse_games(games,l)

game_legality = {}
part_2_answer = 0
for k in games:
    game_legality[k] = is_game_legal(games[k])
    part_2_answer += min_rgb_power(games[k])

print(f'The answer to part 1 is {part_1_answer(game_legality)}.')
print(f'The answer to part 2 is {part_2_answer}.')

