# 56 Merge Intervals

# optimal soluting uisng greedy appraoch
# TC = O(NlogN) and SC = O(N)
def merge(intervals):
    result = []
    intervals.sort()
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result