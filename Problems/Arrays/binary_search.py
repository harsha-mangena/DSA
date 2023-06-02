class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Performs a binary search on a given list to find a target element.
        
        Args:
            nums (List[int]): The list to search.
            target (int): The target element to find.
        
        Returns:
            int: The index of the target element in the list if found, otherwise -1.
        """
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                high = mid-1
            
            else:
                low = mid+1
        return -1