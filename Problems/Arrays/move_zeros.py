class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        initial = 0
        for i in range(len(nums)):
            element = nums[i]
            if element != 0:
                nums[initial], nums[i] = nums[i], nums[initial]
                initial += 1