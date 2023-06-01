"""
Link : https://leetcode.com/problems/count-the-number-of-consistent-strings
"""
class Solution:
    def is_valid_string(self, d, word):
        """
        Check if all characters in a word are in a given dictionary.

        :param d: A dictionary with characters to check.
        :type d: dict
        :param word: A string to check if all its characters in the dictionary.
        :type word: str
        :return: A boolean indicating if all characters in the word are in the dictionary.
        :rtype: bool
        """
        for i in word:
            if i not in d:
                return False
        return True
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        d = {i:True for i in allowed} #O(n)
        count = 0

        for word in words:
            if self.is_valid_string(d, word):
                count += 1
        return count

