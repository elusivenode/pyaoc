def move_taboggan(curr_pos, mv_right, mv_down):
    new_pos = (curr_pos[0] + mv_right, curr_pos[1] + mv_down)
    return new_pos

def pos_has_tree(geo, x_pos, y_pos):
    if geo[y_pos][x_pos % len(geo[y_pos])] == '#':
        return True
    else:
        return False

def trees_encountered_on_slope (mv_r, mv_d):
    current_pos = (0, 0)
    tree_ct = 0
    while current_pos[1] < len(geography) - 1:
        new_pos = move_taboggan(current_pos, mv_r, mv_d)
        current_pos = new_pos
        if pos_has_tree(geography, new_pos[0], new_pos[1]):
            tree_ct += 1
    return tree_ct

with open('/Users/hamish.macdonald/Dev/pyaoc/2020/puzzle_input/day3/input_3.txt', 'r') as input_f:
    input_lines = input_f.readlines()

geography = []
for l in input_lines[:]:
    geography.append(l.strip())

print(f'Answer to part 1: {trees_encountered_on_slope(3,1)}')

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
trees_encountered = 0
trees_encountered_x = 1
for s in slopes:
    trees_encountered_slope = trees_encountered_on_slope(s[0], s[1])
    trees_encountered += trees_encountered_slope
    trees_encountered_x *= trees_encountered_slope
    print(trees_encountered_slope)
    print(trees_encountered)
    print(trees_encountered_x)

print(f'Answer to part 2: {trees_encountered_x}')