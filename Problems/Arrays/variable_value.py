"""
Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations    
"""

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        """
        Calculates the final value of variable x after performing a series of operations.

        :param operations: A list of strings that contains operations to be performed on x.
        :type operations: list[str]
        :return: The final value of x after performing all the operations
        :rtype: int
        """
        x = 0
        # Base Condition
        if len(operations) == 0: return x

        for ops in operations:
            if ops=='--X' or ops=='X--':
                x -= 1
            else:
                x += 1
        return x