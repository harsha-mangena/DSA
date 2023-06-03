class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately, taking one character from each, until one of them is exhausted.

        :param word1: A string
        :type word1: str
        :param word2: A string
        :type word2: str
        :return: A string formed by alternatively taking one character from each input string, until one is exhausted.
        :rtype: str
        """
        newString = ""
        i = j = 0
        while i<len(word1) and j<len(word2):
            newString += word1[i]
            newString += word2[j]
            i += 1
            j += 1
        newString += (word1[i:] or word2[j:])
        return newString
            
            