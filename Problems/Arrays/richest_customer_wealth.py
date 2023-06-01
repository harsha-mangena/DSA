"""
Link : https://leetcode.com/problems/richest-customer-wealth/
"""
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        """
        Finds the maximum wealth amongst all the given accounts.

        :param accounts: A list of lists where each list contains integers representing the wealth of a customer.
        :type accounts: List[List[int]]
        :return: The maximum wealth amongst all the customers.
        :rtype: int
        """
        max_wealth = -10**9
        for money in accounts:
            max_wealth = max(max_wealth, sum(money))
        return max_wealth
