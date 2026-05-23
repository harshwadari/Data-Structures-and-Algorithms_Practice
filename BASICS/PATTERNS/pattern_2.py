# pattern 2 
"""
*
**
***
****
*****
https://www.naukri.com/code360/problems/n-2-forest_6570178?leftPanelTabValue=PROBLEM&count=25&page=1&search=pattern&sort_entity=order&sort_order=ASC
"""
def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()
pattern2(7)