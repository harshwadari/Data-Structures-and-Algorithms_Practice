# Check it there exists a subsequence with sum = k




# TC = O(2^N) and SC = O(N) stack space
def checkSubsequenceSum(self, arr, k):
    def backtrack(idx, total):
        if idx >= len(arr):
            if total == k:
                return True
            return False
        # pick
        if backtrack(idx + 1, total + arr[idx]):
            return True
        # not pick
        return backtrack(idx + 1, total)
    return backtrack(0, 0)