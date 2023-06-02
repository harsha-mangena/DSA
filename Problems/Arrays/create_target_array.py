class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        """
        Creates a target array by inserting elements from nums at specific positions based on index.
        
        Args:
            nums (list[int]): A list of integers to be inserted into the target array.
            index (list[int]): A list of integers representing the index positions to insert the nums elements.
        
        Returns:
            list[int]: The target array with the elements inserted at the specified index positions.
        """
        result = []
        
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        
        return result