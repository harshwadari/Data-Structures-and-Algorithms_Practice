# Quick Sort Algorithm

"""
Inutiution :
1. Pick any one pivot element like first element or middle or last element of array
2. put that pivot element in it's correct position 
3. put all smaller element in left side of pivot and same for right side
4. repeat all untill array is sorted 
"""


#TC = O(NlogN) and SC = Best case recursion stack → O(log n)
# Worst case → O(n)
def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
arr = [5,4,3,2,1]
quicksort(arr,0,len(arr)-1)
print(arr)