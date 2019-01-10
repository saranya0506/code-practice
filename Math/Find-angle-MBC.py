import math

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    radian = math.atan(ab/bc)
    degrees = str(round(math.degrees(radian))) + '\u00b0'
    print(degrees)
