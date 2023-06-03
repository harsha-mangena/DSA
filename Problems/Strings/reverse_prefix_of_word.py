class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Reverses the prefix of a given string up to and including the first occurrence of a given character.
        
        :param word: The input string to be processed.
        :type word: str
        :param ch: The character to search for and reverse the prefix up to and including.
        :type ch: str
        :return: The modified string with the prefix reversed, or the original string if the character is not found.
        :rtype: str
        """
        index = word.find(ch)

        if index == -1:
            return word

        return word[:index+1][::-1]+word[index+1:]