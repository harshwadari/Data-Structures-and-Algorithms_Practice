# TC = O(N) and SC = O(N)
def reverseSubArray( arr, l, r):

        # Convert 1-based indexing to 0-based indexing
        l -= 1
        r -= 1

        def reverse(left, right):
            if left >= right:
                return

            arr[left], arr[right] = arr[right], arr[left]

            reverse(left + 1, right - 1)

        reverse(l, r)

        return arr