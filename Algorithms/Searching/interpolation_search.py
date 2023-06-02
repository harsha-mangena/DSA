def insterpolation_search(arr : list[int], target) -> int: 
    """
    Performs interpolation search on a given sorted array to find the index of a given target element.
    
    Args:
    - arr: A sorted list of integers.
    - target: An integer to be searched in the list.
    
    Returns:
    - If the target is found in the list, returns the index of the target element.
    - If the target is not found in the list, returns -1.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high and arr[low] <= target and arr[high] >= target:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == target:
            return pos 
        
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

arr = [1,2,3,4,5]
target = 5
print(insterpolation_search(arr, target))
