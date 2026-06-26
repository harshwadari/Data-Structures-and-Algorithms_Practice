# Check it there exists a subsequence with sum = k




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