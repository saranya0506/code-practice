'''
Computes the cartesian product.
e.g. product([1,2,3],[3,4]) = (1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)
'''

from itertools import product

def cartesian_product(A, B):
    end_product = product(A, B)
    return (end_product)

if __name__ == '__main__':
    A = map(int, input().split())
    B = map(int, input().split())
    result = cartesian_product(A, B)
    print(*result)
