# pattern 3
"""
1
12
123
1234
12345
"""

def pattern3(n):
    for i in range(n):
        for j in range(1,i+2):
            print(j,end='')
        print()
pattern3(7)
