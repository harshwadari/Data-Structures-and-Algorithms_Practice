# 154. Find Minimum in Rotated Sorted Array II

"""this problem is same as find min element in rotated sorted array but here is has
dubplicates so we will shrink when low mid high are same thats it
"""

# optimal apprach using binary search
# TC = O(logN) and SC = O(1)

def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        mini = float('inf')
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[low] == nums[mid] == nums[high]:
                mini = min(mini,nums[mid])
                low += 1
                high -=1
                continue
            if nums[mid] <= nums[high]:
                if nums[mid] < mini:
                    mini = nums[mid]
                high = mid - 1
            else:
                if nums[low] < mini:
                    mini = nums[low]
                low = mid + 1
        return mini
