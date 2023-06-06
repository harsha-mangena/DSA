def selection_sort(arr):
    """
    Sorts an array in ascending order using the Selection Sort algorithm.
    
    The algorithm works by iterating through the array, 
    finding the minimum element and swapping it with the element at the current index.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list in ascending order.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [1,2,-1,0,100,67]
print(selection_sort(arr))