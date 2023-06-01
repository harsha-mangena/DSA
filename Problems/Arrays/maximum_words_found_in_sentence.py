"""
Link : https://leetcode.com/problems/maximum-number-of-words-found-in-sentences
"""

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        
        max_words = -10**9
        for word in sentences:
            max_words = max(max_words, len(word.split(" ")))
        return max_words
