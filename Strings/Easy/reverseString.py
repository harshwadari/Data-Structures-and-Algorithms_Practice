# Reverse a given String 

"""
Docstring for Strings.Easy.reverseString
Different approaches to reverse a String 
"""


# pythonic way 
# TC = O(N) and SC = O(1)
def reverstring(str):
    return str[::-1]
print(reverstring("hsrah"))


# using loop reversing
# TC = O(N^2) and SC = O(N)
def reverseS(str):
    result = ""
    for i in range(len(str)-1,-1,-1):
        result += str[i]
    return result
print(reverseS('harsh'))


# using two pointer
# TC = O(N) and SC = O(N)
def reverse_string(s):
    arr = list(s)
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return "".join(arr)

print(reverse_string("hello"))



# using stack

