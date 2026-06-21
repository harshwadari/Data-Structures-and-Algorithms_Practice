# Counting Sort
"""
Counting Sort is a non-comparison sorting algorithm. 
Instead of comparing elements, I count the frequency 
of every value using a count array. Then I reconstruct 
the sorted array using those frequencies. Its time complexity 
is O(n + k), where k is the range of values, and space 
complexity is O(k). It is efficient when the value range 
is not significantly larger than the number of elements. 
It can also be made stable using prefix sums and reverse traversal.



When to use

Good when:

n = 100000
values range from 0 to 1000

Then:

Counting Sort -> O(n + 1000)
Comparison Sort -> O(n log n)

Counting sort is often faster.
"""

# TC = O(N + K) and SC = O(K)
def counting_sort(arr):
    if not arr:
        return arr

    max_element = max(arr)

    count = [0] * (max_element + 1)

    # Count frequency
    for num in arr:
        count[num] += 1

    index = 0

    # Reconstruct sorted array
    for value in range(len(count)):
        while count[value] > 0:
            arr[index] = value
            index += 1
            count[value] -= 1

    return arr


arr = [5,4,3,2,1]
print(counting_sort(arr))

