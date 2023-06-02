class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        """
        Finds the concatenation value of the given list of integers.

        Args:
            nums (list[int]): The list of integers to process.

        Returns:
            int: The concatenation value of the given list of integers.
        """
        i = 0
        j = len(nums)-1
        value = 0

        while i<=j:
            if i!=j:
                temp = nums[j]
                while temp:
                    nums[i] *= 10
                    temp = temp // 10
                value += nums[i]+nums[j]
            else:
                value += nums[i]

            i+=1
            j-=1

        return value 