def binary_search(arr : list[int], target) -> int:
    """
    Performs binary search on a sorted list of integers to find the index of a target integer.
    
    :param arr: A sorted list of integers to search through.
    :type arr: list[int]
    :param target: The integer to search for.
    :return: The index of the target integer in the list if it exists, otherwise -1.
    :rtype: int
    """
    if arr is None:
        return -1
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid 
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return -1

array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14
print(binary_search(array, target))