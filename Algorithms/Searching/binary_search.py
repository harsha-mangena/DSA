def binary_search(arr : list[int], target) -> int:
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