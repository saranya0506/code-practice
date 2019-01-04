def create_unique_chars(substr):
    char_list = list(substr)
    unique_char_list = list()
    for x in char_list:
        if x not in unique_char_list:
            unique_char_list.append(x)
    return ''.join(unique_char_list)

def merge_the_tools(string, k):
    subsegment = list()
    for i in range(0, len(string), k):
        subsegment.append(string[i:i+k])
    #print(subsegment)
    result = [create_unique_chars(i) for i in subsegment]
    print(*result, sep='\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
