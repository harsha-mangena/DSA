class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        """
        Calculates the number of words in a list of strings that have their first and last characters as vowels.
        
        :param words: A list of strings where each string represents a word.
        :type words: list[str]
        :param left: An integer representing the starting index of the subarray.
        :type left: int
        :param right: An integer representing the ending index of the subarray.
        :type right: int
        :return: An integer representing the number of words in the subarray with first and last characters as vowels.
        :rtype: int
        """

        vowels = set('aeiou')
        
        return sum({w[0],w[-1]}.issubset(vowels) for w in words[left:right+1])