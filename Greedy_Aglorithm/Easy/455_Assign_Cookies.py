# Assign Cookies lc 455

# Optimal Approach using Greedy Apprach

# TC = O(NlogN + MlogM) and SC = O(m+n) or O(logm+logn)
def cookies(greedy: list[int],childs: list[int])-> int:
    greedy.sort()
    childs.sort()
    i = 0
    j = 0
    cookies_Assigned = 0
    while i < len(greedy) and j < len(childs):
        if greedy[i] <= childs[j]:
            cookies_Assigned += 1
            i += 1
        j += 1
    return cookies_Assigned