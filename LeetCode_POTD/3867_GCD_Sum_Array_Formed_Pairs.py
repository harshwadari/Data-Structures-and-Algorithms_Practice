# 3867. Sum of GCD of Formed Pairs
"""
You are given an integer array nums of length n.

Construct an array prefixGcd where for each index i:

Let mxi = max(nums[0], nums[1], ..., nums[i]).
prefixGcd[i] = gcd(nums[i], mxi).
After constructing prefixGcd:

Sort prefixGcd in non-decreasing order.
Form pairs by taking the smallest unpaired element and the largest unpaired element.
Repeat this process until no more pairs can be formed.
For each formed pair, compute the gcd of the two elements.
If n is odd, the middle element in the prefixGcd array remains unpaired and should be ignored.
Return an integer denoting the sum of the GCD values of all formed pairs.

The term gcd(a, b) denotes the greatest common divisor of a and b.
 

Example 1:

Input: nums = [2,6,4]

Output: 2

Explanation:

Construct prefixGcd:

i	nums[i]	mxi	prefixGcd[i]
0	2	2	2
1	6	6	6
2	4	6	2
prefixGcd = [2, 6, 2]. After sorting, it forms [2, 2, 6].

Pair the smallest and largest elements: gcd(2, 6) = 2. The remaining middle element 2 is ignored. 
Thus, the sum is 2.

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 10​​​​​​​9
"""

# Optimal approach
"""
Overall Time Complexity
O(N log M) + O(N log N) + O(N log M)

which simplifies to

O(N log N + N log M)

where:

N = number of elements
M = maximum value in the array

SC = O(N)
"""
class Solution:
    def gcd(self,a:int,b:int)-> int:
        while b != 0:
            a , b = b , a % b
        return a
    def gcdSum(self,nums:list[int]) -> int:
        total = 0
        prefixgcd = []
        largest = nums[0]
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
            prefixgcd.append(self.gcd(nums[i],largest))
        prefixgcd.sort()
        i = 0
        j = len(prefixgcd) - 1
        while i < j:
            total += self.gcd(prefixgcd[i],prefixgcd[j])
            i += 1
            j -= 1
        return total
obj = Solution()
print(obj.gcdSum([3,6,2,8]))