def sum_to_something(l,s):
    for i,x in enumerate(l):
        for y in l[i+1:]:
            if x + y == s:
                return (x,y)
    return (-1,-1)

def sum_to_something_else(l,s):
    for i,x in enumerate(l):
        for y in l[i+1:]:
            for z in l[i + 2:]:
                if x + y + z == s:
                    return (x,y,z)
    return (-1,-1,-1)

with open('/Users/hamish.macdonald/Dev/pyaoc/2020/puzzle_input/day1/input_1.txt', 'r') as input_f:
    input_lines = input_f.readlines()

expenses = []
for l in input_lines[:]:
    expenses.append(int(l.strip()))

x,y = sum_to_something(expenses,2020)
print(f'Answer to part 1: {x*y}')

x,y,z = sum_to_something_else(expenses,2020)
print(f'Answer to part 2: {x*y*z}')

