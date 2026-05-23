"""

Recursion is when a function calls itself to solve a smaller version of the same problem.

Two important parts:

Base case → condition to stop recursion

Recursive call → function calling itself with smaller input

If you miss the base case → infinite recursion → stack overflow.



The recursive stack (or call stack) is a memory structure that stores
information about each active function call, including local variables 
and return addresses.  Every time a recursive function is invoked, a new 
stack frame is pushed onto this stack.  As the function calls itself, the 
stack grows deeper, consuming memory resources until the base case is reached 
and frames are popped off. 



A stack overflow error occurs when the recursive stack exceeds its allocated memory limit.  
This typically happens due to infinite recursion (missing or unreachable base case) or 
excessive recursion depth (too many calls before stopping).


Backtracking: The recursive call is not the last operation. 
The key steps happen after the function call returns.
"""


# Infininte recursion without any base condition 
def greet():
    print("greeting")
    greet()
# greet()


def print_n_times(n:int):
    if n == 0:          # Base case
        return
    
    print("Hello")      # Work
    print_n_times(n-1)  # Recursive call


print_n_times(5)



# print 1 to N using recursion

def OnetoN(n):
    if n == 0:
        return
    OnetoN(n-1)
    print(n)
print(OnetoN(10))



# sum of first N using recursion

def sumN(n):
    if n == 0:
        return 0
    return n + sumN(n-1)
# print(sumN(5))


# factorial using recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
# print(factorial(10))