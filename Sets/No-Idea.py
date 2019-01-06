if __name__ == '__main__':
    n, m = map(int, input().split())
    list_of_int = list(input().split())
    set_a = set(input().split())
    set_b = set(input().split())
    happiness = 0
    for i in list_of_int:
        if i in set_a:
            happiness += 1
        elif i in set_b:
            happiness -= 1
    print(happiness)
