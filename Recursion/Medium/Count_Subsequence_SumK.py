# Count all Subsequences with sum k
# TC = O(2^N) and SC = O(N)
def countSubsequenceSum(arr, k):

    def backtrack(idx: int, total: int):

        # Base case
        if idx == len(arr):
            if total == k:
                return 1
            else:
                return 0

        # Pick current element
        left = backtrack(idx + 1, total + arr[idx])

        # Don't pick current element
        right = backtrack(idx + 1, total)

        # Total valid subsequences
        return left + right

    return backtrack(0, 0)