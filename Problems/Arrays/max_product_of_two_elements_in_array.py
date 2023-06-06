class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Returns the maximum product of two integers that are one less than two largest integers in the input list.
        
        Args:
            nums (List[int]): A list of integers.
        
        Returns:
            int: The maximum product of two integers that are one less than two largest integers in the input list.
        """
        nums.sort()
        return max((nums[-1]-1)*(nums[-2]-1), (nums[0]-1)*(nums[1]-1))