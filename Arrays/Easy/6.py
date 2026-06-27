#to rotate array by d place

# brute force method
#TC = O(N*R) where r is number of rotations and SC = O(N)

# def rotate(nums,k):
#     n = len(nums)
#     rot = k%n
#     for _ in range(0,rot):
#         e = nums.pop()
#         nums.insert(0,e)


# # better approach using slicing
# # TC = O(N) and SC = O(1)
# def rota(nums,k):
#     n = len(nums)
#     k = k%n
#     nums[:] = nums[n-k:] + nums[:n-k]
#     return nums


# optimal approach using reverse algorithm
# TC + O(N) and SC = O(1)

def rota1(nums,k):
    n  = len(nums)
    k = k%n
    def reve(left,right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1
    
    reve(0,n-1)
    reve(0,k-1)
    reve(k,n-1)
    return nums

print(rota1([1,2,3,4,5],3))
