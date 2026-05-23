import sys

def main():
    data = sys.stdin.read().strip().split()
    idx = 0

    # number of piles
    n = int(data[idx])
    idx += 1

    # pile sizes
    arr = []
    for i in range(n):
        arr.append(int(data[idx]))
        idx += 1

    # hours limit
    h = int(data[idx])

    low = 1
    high = max(arr)

    while low <= high:
        mid = (low + high) // 2
        hours = 0

        for i in range(n):
            hours += (arr[i] + mid - 1) // mid

        if hours <= h:
            high = mid - 1
        else:
            low = mid + 1

    print(low)

if __name__ == "__main__":
    main()
