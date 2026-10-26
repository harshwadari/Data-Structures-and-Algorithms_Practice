# Minimum Swaps to Sort
"""
Given an array arr[] of distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.

Examples:

Input: arr[] = [2, 8, 5, 4]
Output: 1
Explanation: Swap 8 with 4 to get the sorted array.
Input: arr[] = [10, 19, 6, 3, 5]
Output: 2
Explanation: Swap 10 with 3 and 19 with 5 to get the sorted array.
Input: arr[] = [1, 3, 4, 5, 6]
Output: 0
Explanation: Input array is already sorted.
Constraints:

1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 109

"""


class Solution:
    def minSwaps(self, arr):
        n = len(arr)

        arr_pos = []
        for i in range(n):
            arr_pos.append((arr[i], i))

        arr_pos.sort()

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr_pos[i][1] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr_pos[j][1]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps