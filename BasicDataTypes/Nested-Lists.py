def find_second_lowest_grade(students):
    names = list()
    second_lowest = sorted(list(set(score for name, score in students)))[1]
    for i in students:
        if i[1] == second_lowest:
            names.append(i[0])
    return names

if __name__ == '__main__':
    students = list()
    for _ in range(int(input())):
        students.append([input(), float(input())])
    result = find_second_lowest_grade(students)
    result.sort()
    print(*result, sep='\n')


