'''

itertools.permutations(iterable[, r]) - returns successive r length permutations of elements in an iterable.
if the iterable is sorted, it will return permutations in lexicographic sortedorder

'''

from itertools import permutations

if __name__ =='__main__':
    str, length = input().split()
    result = sorted(list(permutations(str, int(length))))
    for _ in result:
        print(''.join(_))
