class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        """
        Given a list of integers `nums`, this function counts the number of hills and valleys. A hill is defined as a sequence of adjacent integers that are strictly increasing, followed by a sequence of adjacent integers that are strictly decreasing. A valley is defined as a sequence of adjacent integers that are strictly decreasing, followed by a sequence of adjacent integers that are strictly increasing. The function returns the total number of hills and valleys in the input list.

        Args:
        - nums: A list of integers.

        Returns:
        - An integer representing the total number of hills and valleys in the input list.
        """
        hills_valleys = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            elif nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                hills_valleys += 1
            elif nums[i-1] > nums[i] and nums[i] < nums[i+1]:
                hills_valleys += 1
            
        return hills_valleys
