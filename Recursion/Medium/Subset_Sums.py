def subsetSums(arr):
	# code here
	result = []
	def backtrack(index,total):
		if index >= len(arr):
			result.append(total)
			return
		backtrack(index + 1,total)
		backtrack(index + 1,total + arr[index])
	backtrack(0,0)
	return result
		