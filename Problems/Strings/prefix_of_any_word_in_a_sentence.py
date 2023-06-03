class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Returns the index of the first word in the given sentence that starts with the given search word, or -1 if no such word is found.

        :param sentence: A string representing the sentence to search in.
        :type sentence: str
        :param searchWord: A string representing the search word.
        :type searchWord: str
        :return: An integer representing the index of the first word in the sentence that starts with the search word, or -1 if no such word is found.
        :rtype: int
        """
        index = 0
        l = len(searchWord)
        for word in sentence.split(' '):
            index += 1
            if word[:l] == searchWord:
                return index
        return -1