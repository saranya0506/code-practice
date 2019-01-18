from itertools import product

if __name__ =='__main__':
    K, M = map(int, input().split())
    L = list()
    for i in range(K):
        L.append(list(input().split())[1:])
    print(L)
    prod = list(product(*L))
    result = map(lambda x : sum(i**2 for i in map(int, x))%M, prod)
    max_val_lst = list(result)
    print(max(max_val_lst))
