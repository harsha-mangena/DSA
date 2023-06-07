class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Checks whether a given integer is a palindrome or not.
        
        :param x: An integer to be checked.
        :type x: int
        
        :return: Returns True if the given integer is a palindrome, False otherwise.
        :rtype: bool
        """
        if x < 0:
            return False
        
        return str(x) == str(x)[::-1]