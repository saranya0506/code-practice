'''
itertools.combinations(iterable, r)

Permutations are for lists (order matters) and combinations are for groups (order doesn’t matter)
Permutations - AH and HA are different
Combinations - AH and HA are considered same
'''

from itertools import combinations

if __name__ =='__main__':
    str, length = input().split()
    for i in range(1, int(length)+1):
        result = list(combinations(sorted(list(str)), i))   
        for _ in result:
            print(''.join(_))
