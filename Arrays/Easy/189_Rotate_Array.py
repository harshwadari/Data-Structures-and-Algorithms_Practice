# 189. Rotate Array
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three 
different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""










# brute force method 
# TC = O(N*R) where r is number of rotations and SC = O(N)

def rotate(nums,k):
    n = len(nums)
    rot = k%n
    for _ in range(0,rot):
        e = nums.pop()
        nums.insert(0,e)


# better approach using slicing
# TC = O(N) and SC = O(1)
def rota(nums,k):
    n = len(nums)
    k = k%n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums


# optimal approach using reverse algorithm
# TC + O(N) and SC = O(1)

def rota1(nums,k):
    n  = len(nums)
    k = k%n
    def reve(left,right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1
    
    reve(0,n-1)
    reve(0,k-1)
    reve(k,n-1)
    return nums

print(rota1([1,2,3,4,5],3))
