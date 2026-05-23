# patter 5
"""
******
*****
****
***
**
*
"""

def pattern5(n):
    for i in range(1,n):
        for j in range(1,(n-i)+1):
            print('*',end='')
        print()
pattern5(7)