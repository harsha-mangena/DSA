def linear_search(arr :list[int], element) -> int:
    """
    Performs a linear search on the input list `arr` to find the first occurrence of `element`. 
    The function returns the index of the element if it exists in the list, otherwise, it returns -1. 

    Args:
    - arr (list[int]): The input list of integers to search.
    - element : The element to search for in the list.

    Returns:
    - int : The index of the element in the list if it exists, otherwise -1.
    """
    if len(arr) == 0:
        return -1
    
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    
    return -1
    
arr = [1,2,-1,0,100,67]
element = 0
print(linear_search(arr, element))
    