# pattern 1
"""
*****
*****
*****
*****
*****

https://www.naukri.com/code360/problems/triangle-star-pattern_626546?leftPanelTabValue=PROBLEM&count=25&page=1&search=pattern&sort_entity=order&sort_order=ASC&customSource=studio_nav
"""

"""
Patter -> Nested loops
 1. for the outer loop , focus on number of rows
 2. for the inner loop , focus on the columns and connect some how to rows
 3. print them inside the outer loop or just after finishing inner loop
 4. observe symmetry [optional] only on specific patterns 
"""

def pattern1(n:int):
    for i in range(n):
        for j in range(n):
            print('*',end="")
        print()
pattern1(7)