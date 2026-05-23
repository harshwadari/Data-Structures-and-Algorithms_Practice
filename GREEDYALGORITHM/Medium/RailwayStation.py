# Minimum Platforms

# optimal solution using greedy
# TC = O(N logN) and SC = O(1)
def minplatform(arr,dep):
    i = 1
    j = 0
    count = 1
    ans = 1
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        ans = max(ans, count)
    return ans 