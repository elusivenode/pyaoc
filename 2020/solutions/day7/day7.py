import re

def get_bags(b,d,chain):
    #print(b)
    #print(d[b])
    for i in d[b]:
        #print(i)
        i_rm_ct,_ = i.split(':')
        #print(i_rm_ct)
        chain += f',{i}'
        if i_rm_ct in d:
            #print(f'{i} {d[i]}')
            chain = get_bags(i_rm_ct,d,chain)
    return chain

def has_shiny_gold(chain):
    ct = 0
    #print(chain)
    for b in chain.split(','):
        #print(b)
        if len(b) > 0:
            bc,_ = b.split(':')
            #print(bc)
            if bc == 'shiny gold':
                ct += 1
                #print(ct)
    return ct

with open('/Users/hamish.macdonald/Dev/pyaoc/2020/puzzle_input/day7/input_7.txt', 'r') as input_f:
    input_lines = input_f.readlines()

pattern = r'[0-9]'
bag_rules_l = []
for l in input_lines[:]:
    l = l.replace('bags', 'bag')
    l = l.replace('bag', '')
    l = l.replace('.', '')
    bag_rules_l.append(l.strip())

bag_rules_d = {}
for rule in bag_rules_l:
    k,v = rule.split('contain')
    bags_l = []
    for bag in v.split(','):
        match = re.search(pattern,bag)
        n = '0'
        if match:
            n = str(match.group())
        bag = re.sub(pattern, '', bag).strip() + ':' + n
        bags_l.append(bag)
    bag_rules_d[k.strip()] = bags_l

bag_chains = {}
for k in bag_rules_d:
    bag_chain = ''
    bag_chains[k] = get_bags(k, bag_rules_d, bag_chain)
#print(bag_chains)
chains_with_shiny_gold = 0
for k in bag_chains:
    if has_shiny_gold(bag_chains[k]) > 0:
        chains_with_shiny_gold += 1

print(f'The answer to part 1 is {chains_with_shiny_gold}')

def ct_bags_within(root_bag, rules_d, multiplier, bag_ct):
    for r in rules_d[root_bag]:
        b, ct = r.split(':')
        ct = int(ct)
        multiplier *= multiplier
        bag_ct += ct * multiplier
        if b != 'no other':
            bag_ct = ct_bags_within(b,rules_d, ct, bag_ct)
    return bag_ct

print(f'The answer to part 2 is {ct_bags_within("shiny gold", bag_rules_d, 1,0)}')
