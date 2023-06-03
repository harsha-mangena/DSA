from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        Determines if the number of occurrences of each character in a given string are equal.

        :param s: The input string to check.
        :type s: str
        :return: True if the number of occurrences of each character is equal, False otherwise.
        :rtype: bool
        """
        d = defaultdict(int)
        for i in s: d[i] += 1
        c = d[s[0]]
        for i in d:
            if d[i] != c: return 0
        return 1