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
    return result


# Optimal appraoch using recursive backtracking
# TC = O(2^N) and SC = O(N) stack space
def subsequence(arr: list[int], target:int) ->int:
    result = []
    def backtrack(index,total,subset):
        if index >= len(arr):
            if total == target:
                result.append(subset[:])
            return 
        subset.append(arr[index])
        backtrack(index + 1,total + arr[index],subset)
        subset.pop()
        backtrack(index + 1,total,subset)
    backtrack(0,0,[])
    return result
