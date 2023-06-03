class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if a given string is a palindrome.
        
        :param s: the string to check.
        :type s: str
        
        :return: True if the string is a palindrome, False otherwise.
        :rtype: bool
        """
        if len(s) == 0: return False

        s = s.lower()

        check_str = ''.join(i for i in s if i.isalnum())

        return check_str == check_str[::-1]