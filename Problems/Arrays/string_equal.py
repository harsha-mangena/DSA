"""
Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent
"""

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        """
        Compares two arrays of strings and returns True if they are equal,
        False otherwise.

        Args:
            word1 (list[str]): The first array of strings to compare.
            word2 (list[str]): The second array of strings to compare.

        Returns:
            bool: True if the two arrays of strings are equal, False otherwise.
        """
        #Base & Final Condition
        str1=''.join(word1)
        str2=''.join(word2)
        return str1==str2
        