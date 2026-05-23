# pattern 4
"""
1
22
333
4444
55555
"""
def pattern4(n):
    for i in range(n):
        for j in range(1,i+2):
            print(i+1,end=" ")
        print()
pattern4(7)