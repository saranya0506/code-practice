'''
itertools.combinations_with_replacement(iterable, r)

This tool returns r length subsequences of elements from the input iterable allowing individual elements 
to be repeated more than once.

e.g. HACK 2

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

'''

from itertools import combinations_with_replacement

if __name__ =='__main__':
    str, length = input().split()
    result = list(combinations_with_replacement(sorted(list(str)), int(length)))
    for i in result:
        print(''.join(i))
