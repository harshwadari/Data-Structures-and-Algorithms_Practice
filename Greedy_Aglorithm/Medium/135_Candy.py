# Lc 135 Candy problem 

# better approach 
# TC = O(3N) and SC = O(2N)

def candies(ratings):
    n = len(ratings)
    left = [1] * n
    right = [1] * n
    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            left[i] = left[i-1] + 1
    for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            right[i] = right[i+1] + 1
    total = 0
    for i in range(n):
        total += max(left[i], right[i])
    return total


# str = [1000] -> 3
# str = [100101] -> 2

def seats(str:list[str]) -> int:
    n = len(str)
    maxdist = 0
    for i in range(n):
        distance = 0
        if str[i] == '0':
            distance += 1
            maxdist = max(distance, maxdist)
        continue
    return maxdist
print(seats('1000'))