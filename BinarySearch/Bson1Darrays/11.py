# find out how many times arr is rotated

# brut first we have to fin min the return min index

def brut(nums):
    mini = float('inf')
    index= -1
    for i in range(len(nums)):
        mini = min(mini,nums[i])
        index = i