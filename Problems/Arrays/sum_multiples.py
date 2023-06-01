"""
Link: https://leetcode.com/problems/sum-multiples/
"""
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        """
        Calculates the sum of all multiples of 3, 5, and 7 up to n (inclusive).

        :param n: An integer representing the upper bound of the range of numbers to
                  consider.
        :return: An integer representing the sum of all multiples of 3, 5, and 7 up to
                 n (inclusive).
        """
        sum = 0
        for i in range(n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum += i
        return sum