# 3300. Minimum Element After Replacement With Digit Sum

# optimal approach using digit extraction and calculating the sum of digits
# TC = O(N * logM) where N is the number of elements in the array and M is the maximum element in the array, and SC = O(1)
def minElement(nums):
    result = float('inf')
    for num in nums:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        result = min(result, digit_sum)
    return result