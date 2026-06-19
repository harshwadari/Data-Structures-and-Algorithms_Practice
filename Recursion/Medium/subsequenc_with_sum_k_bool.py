class Solution:
    def checkSubsequenceSum(self, arr, k):

        def backtrack(idx, total):
            if idx >= len(arr):
                return total == k

            # pick
            if backtrack(idx + 1, total + arr[idx]):
                return True

            # not pick
            return backtrack(idx + 1, total)

        return backtrack(0, 0)