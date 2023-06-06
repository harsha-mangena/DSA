def insertion_sort(arr):
    """
    Sorts a given list of integers using the insertion sort algorithm.
    
    The algorithm works by iterating through the list and for each element, 
    it compares it to the elements before it and 
    inserts it in the correct position in the sorted part of the list.

    Parameters:
    arr (list[int]): The unsorted list of integers to be sorted.

    Returns:
    list[int]: The sorted list of integers.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    
    return arr 

arr = [1,2,-1,0,100,67]
print(insertion_sort(arr))