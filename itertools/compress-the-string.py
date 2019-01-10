# Brute force

from itertools import groupby

if __name__ =='__main__':
    str = input()
    result = list()
    for i in [list(g) for k, g in groupby(str)]:
        result += [(sum(1 for i in v), int(k)) for k, v in groupby(i)]
    print(*result, sep=' ')
    
#Better solution - only one groupby

from itertools import groupby

if __name__ =='__main__':
    str = input()
    result = list()
    result = [(len(list(v)), int(k)) for k, v in groupby(str)]
    print(*result, sep=' ')

