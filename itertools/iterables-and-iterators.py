'''

Sample Input
4 
a a c d
2

Sample Output
0.8333

Explanation
All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd'), ('c', 'd')
Out of these  combinations, 5 of them contain either index 0 or index 1 which are the indices that contain the letter 'a'.
Hence, the answer is 5/6 = 0.833.

'''

from itertools import combinations

if __name__ =='__main__':
    N = int(input())
    str = list(input().split())
    K = int(input())
    combn = list(combinations(str, K))
    print(combn)
    count = 0
    for item in combn:
        if 'a' in item and (lambda t : t[i] for i in range(K)):
            count += 1
    print(count/len(combn))
