import sys

def canPartition(nums):
    n = len(nums)
    total = sum(nums)

    if total % 2:
        return False

    target = total // 2
    dp = [[-1] * (target + 1) for _ in range(n)]

    def backtrack(index, curr):
        if curr == 0:
            return True

        if index == 0:
            return nums[0] == curr

        if dp[index][curr] != -1:
            return dp[index][curr]

        pick = False
        if nums[index] <= curr:
            pick = backtrack(index - 1, curr - nums[index])

        notpick = backtrack(index - 1, curr)

        dp[index][curr] = pick or notpick
        return dp[index][curr]

    return backtrack(n - 1, target)


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    print(canPartition(nums))


if __name__ == "__main__":
    main()