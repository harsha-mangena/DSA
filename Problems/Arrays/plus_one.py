class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Takes in a list of integers, representing a number, and returns a new list
        corresponding to the number plus one. The list must not contain any leading
        zeros. The function returns a list of integers.

        :param digits: A list of integers representing a number.
        :type digits: List[int]
        :return: A list of integers representing the number plus one.
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits