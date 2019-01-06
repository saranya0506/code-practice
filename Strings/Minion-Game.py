# Brute Force (Timed out for few test cases)
def minion_game(string):
    vowels = list('AEIOU')
    str_upper = string.upper()
    ln =  len(str_upper)
    all_unique_substrings = list(set(str_upper[i:j+1] for i in range(ln) for j in range(i, ln)))
    substring_with_vowels = list()
    substring_with_consonants = list()
    for i in all_unique_substrings:
        if i[0] not in vowels:
            substring_with_consonants.append(i)
        else:
            substring_with_vowels.append(i)
    #print(substring_with_vowels)
    #print(substring_with_consonants)

    kevin_score = 0
    for s in substring_with_vowels:
        for i in range(ln):
            if s == str_upper[i:i+len(s)]:
                kevin_score += 1

    stuart_score = 0
    for s in substring_with_consonants:
        for i in range(ln):
            if s == str_upper[i:i+len(s)]:
                stuart_score += 1

    if kevin_score >= stuart_score:
        if kevin_score == stuart_score:
            print('Draw')
        else:
            print('Kevin', kevin_score)
    else:
        print('Stuart', stuart_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)

# Optimal solution
def minion_game(string):
    vowels = list('AEIOU')
    ln = len(string)
    kevin_score = 0
    stuart_score = 0
    for i in range(ln):
        if s[i] in vowels:
            kevin_score += (ln-i)
        else:
            stuart_score += (ln-i)

    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif kevin_score < stuart_score:
        print ('Stuart', stuart_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
