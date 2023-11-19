import re

def get_bags(b,d,chain):
    for i in d[b]:
        chain += f',{i}'
        if i in d:
            #print(f'{i} {d[i]}')
            chain = get_bags(i,d,chain)
    return chain

def has_shiny_gold(chain):
    ct = 0
    for b in chain.split(','):
        if b == 'shiny gold':
            ct += 1
    return ct

with open('/Users/hamish.macdonald/Dev/pyaoc/2020/puzzle_input/day7/input_7.txt', 'r') as input_f:
    input_lines = input_f.readlines()

pattern = r'[0-9]'
bag_rules_l = []
for l in input_lines[:]:
    l = l.replace('bags', 'bag')
    l = l.replace('bag', '')
    l = l.replace('.', '')
    l = re.sub(pattern, '', l)
    bag_rules_l.append(l.strip())

bag_rules_d = {}
for rule in bag_rules_l:
    k,v = rule.split('contain')
    bags_l = []
    for bag in v.split(','):
        bags_l.append(bag.strip())
    bag_rules_d[k.strip()] = bags_l

bag_chains = {}
for k in bag_rules_d:
    bag_chain = ''
    bag_chains[k] = get_bags(k, bag_rules_d, bag_chain)

chains_with_shiny_gold = 0
for k in bag_chains:
     if has_shiny_gold(bag_chains[k]) > 0:
         chains_with_shiny_gold += 1

print(f'The answer to part 1 is {chains_with_shiny_gold}')