# Generate Subsequence with sum equal to k 
#  brut approach is by generating all the subsequence and check sum before appending into result  
# TC = O( N *2^N) and SC = O(N)
def subsets(nums:list[int],target:int) -> list[list[int]]:
    result = []
    def solver(idx, subset):
        if idx >= len(nums):
            if sum(subset) == target:
                return
            result.append(subset[:])
            return 
        #pick
        subset.append(nums[idx])
        solver(idx + 1,subset)
        # not pick 
        subset.pop()
        solver(idx + 1, subset)
    solver(0,[])
    return len(result)


# Optimal appraoch using recursive backtracking
""" 
class Solution:
	def perfectSum(self, arr, target):
		# code here
		result = []
		def solver(idx,total,subset):
		    if idx >= len(arr):
		        if total == target:
		            result.append(subset[:])
		        return
		    subset.append(arr[idx])
		    solver(idx + 1,total + arr[idx] ,subset)
		    subset.pop()
		    solver(idx + 1,total ,subset)
		solver(0,0,[])
		return len(result)
"""