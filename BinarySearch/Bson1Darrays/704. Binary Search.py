# Linear Search
# TC = O(N) and SC = O(1)

def ls(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1
print(ls([1,2,3,4,5],9))


# Binary Search
# TC = O(logN) and SC = O(1)
def bs(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

# This if for single test cases in OA
def main():
    n = int(input())
    nums = list(map(int,input().split()))
    target = int(input())
    print(bs(nums,target))
if __name__ == '__main__':
    main()


# For Multiple Test case 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int,input().split()))
        target = int(input())
        print(bs(nums,target))
if __name__ == "__main__":
    main()



# Binary Search Using Recursion 
# TC = O(logN) and SC = O(logN) stack space 
def recursionBS(nums, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2 

    if nums[mid] == target:
        return mid
                                                                                                                                                                                                                                                        
    elif nums[mid] < target:
        return bs(nums, target, mid + 1, high)

    else:
        return bs(nums, target, low, mid - 1)