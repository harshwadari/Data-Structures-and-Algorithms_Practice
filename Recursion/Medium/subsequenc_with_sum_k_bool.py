# Check it there exists a subsequence with sum = k


# https://www.geeksforgeeks.org/problems/check-if-there-exists-a-subsequence-with-sum-k/1

# TC = O(2^N) and SC = O(N) stack space
def checkSubsequenceSum(arr:list[int], k:int)->bool:
    def backtrack(idx, total):
            if idx == len(arr):
                if total == k:
                    return True
                else:
                    return False
    
            # Pick the current element
            pick = backtrack(idx + 1, total + arr[idx])
    
            if pick == True:
                return True
            else:
                # Not pick the current element
                not_pick = backtrack(idx + 1, total)
    
                if not_pick == True:
                    return True
                else:
                    return False
    
    return backtrack(0, 0)




# generate  anyone subset with sum k 

def subsequence(arr, target):

    def backtrack(index, total, subset):

        if index == len(arr):
            if total == target:
                print(subset)
                return True
            return False

        # Take
        subset.append(arr[index])

        if backtrack(index + 1, total + arr[index], subset):
            return True

        # Backtrack
        subset.pop()

        # Not take
        if backtrack(index + 1, total, subset):
            return True

        return False

    backtrack(0, 0, [])
print(subsequence([1,2,3],1))