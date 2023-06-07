class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given a list of integers 'nums' and an integer 'target', this function returns a list with the indices of the two numbers that add up to the target.

        Args:
            nums (list[int]): A list of integers.
            target (int): The integer target to find the sum of two integers in the 'nums' list.

        Returns:
            list[int]: A list with the indices of the two numbers that add up to the 'target'. Returns an empty list if no pair is found.
        """
        #Base Condition
        if len(nums)==0:
            return []
        visited = dict()
        for i in range(len(nums)):
            if target-nums[i] in visited:
                return [visited[target-nums[i]], i]
            else:
                visited[nums[i]] = i
        