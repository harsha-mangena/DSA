class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        """
        Calculates the difference between the sum of all digits in a list of integers, and the sum of the integers themselves.

        :param nums: a list of integers to calculate the difference of sum from
        :type nums: list[int]
        :return: the difference between the sum of all digits in `nums` and the sum of `nums` itself
        :rtype: int
        """
        sum_of_each = 0
        sum_of_nums = 0
        for number in nums:

            sum_of_nums += number
            while number:
                sum_of_each = sum_of_each+(number%10)
                number = number // 10
            
        return abs(sum_of_nums - sum_of_each)