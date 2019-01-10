'''
if n=5, output should be the below palindrome triangle :-
1
121
12321
1234321
123454321

Formula derived :-
1         - (1*1)/(1^2)
121       - (22*22)/(2^2)
12321     - (333*333)/(3^2)
1234321   - (4444*4444)/(4^2)

To calculate pattern 1,22,333,4444,etc :-

Geometric  Progression - a, ar, ar^2, ar^3, etc
Sum of n terms = a(r^n -1)
                 ---------
                 (r-1)
a = n, r = 10
'''

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(round(((10**i-1)//9)**2))
