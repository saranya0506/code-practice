import cmath

if __name__ == '__main__':
    z = complex(input())
    r, phase = cmath.polar(z)
    print(r)
    print(phase)
