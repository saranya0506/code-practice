'''

Median on a hypotenuse divides the right angled triangle into 2 isosceles triangle.
AM = BM = CM, <MBC = <MCB
Hence as per "SOHCAHTOA", apply TOA i.e. tan = Oposite/Adjacent (provides ratio)
atan - provides radian

Refer https://www.mathsisfun.com/algebra/trig-finding-angle-right-triangle.html

'''

import math

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    radian = math.atan(ab/bc)
    degrees = str(round(math.degrees(radian))) + '\u00b0'
    print(degrees)
