# 1248. Count Number of Nice Subarrays

# optimal solution 

def nicesubarray(nums,k):
    return atmost(nums,k) - atmost(nums,k-1)
def atmost(nums,k):
    if k < 0:
        return 0 
    left = 0
    sum = 0
    count = 0
    for right in range(len(nums)):
        sum += nums[right] % 2
        while sum > k:
            sum -= nums[left] % 2
            left +=1
        count += right - left + 1
    return count