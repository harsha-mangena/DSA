def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    Args:
    - arr: a list or array of comparable elements to be sorted
    
    Returns:
    - The original array sorted in ascending order
    """
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print(numbers)