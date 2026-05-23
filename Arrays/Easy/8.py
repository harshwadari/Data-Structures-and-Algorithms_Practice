# find missing number in an array
# TC = O(1) and SC = O(1)
def missing(nums):
    n = len(nums)
    result  = 0
    actual_sum = n*(n+1)//2
    expected_sum = sum(nums)
    result = actual_sum - expected_sum
    return result
print(missing([1,2,3,4,5,7,8,9]))