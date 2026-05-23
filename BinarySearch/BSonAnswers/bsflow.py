import sys

def can_make(day, arr, m, k):
    bou = 0
    flow = 0

    for x in arr:
        if x <= day:
            flow += 1
            if flow == k:
                bou += 1
                flow = 0
        else:
            flow = 0

    return bou >= m


def main():
    data = sys.stdin.read().strip().split()
    idx = 0

    n = int(data[idx]); idx += 1
    arr = list(map(int, data[idx:idx+n]))
    idx += n

    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    if m * k > n:
        print(-1)
        return

    low = min(arr)
    high = max(arr)
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if can_make(mid, arr, m, k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)

if __name__ == "__main__":
    main()
