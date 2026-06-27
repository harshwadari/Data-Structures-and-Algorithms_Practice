# 77. Combinations
"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""
"""
ime Complexity: 
O((
k
n
	​

)×k)
	​

Auxiliary Space: 
O(k)
	​

Including output: 
O((
k
n
	​

)×k)
	​

"""
# Optimal approach using recursion backtracking 
def combine(n:int, k:int) -> list[list[int]]:
    result = []
    def backtrack(index:int,subset:list[int]):
        if len(subset) == k:
            result.append(subset[:])
            return
        for i in range(index,n+1):
            subset.append(i)
            backtrack(i + 1,subset)
            subset.pop()
    backtrack(1,[])
    return result