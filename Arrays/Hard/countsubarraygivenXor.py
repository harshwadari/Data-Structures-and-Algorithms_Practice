# Count subarray with given xor 

# brute foce is extrme naive like using 3 nested for loops 



# better approach is using 2 nested for loops
# TC = O(N^2) and SC = O(1)

def subarrayXor(self, arr, k):
        # code here
        count = 0
        for i in range(len(arr)):
            xor = 0
            for j in range(i , len(arr)):
                xor = xor ^ arr[j]
                if xor == k:
                    count +=1
        return count



# optimal approach 