class Solution:
    def get_the_value(self, word):
        """
        Given a string 'word', this function calculates the value of the string
        using the formula (value*10) + (ord(i)-97) for each character in the string.
        'value' is initialized to 0. The function returns the calculated value.

        :param word: A string for which the value is to be calculated.
        :type word: str
        :return: The value of the input string 'word'.
        :rtype: int
        """
        value = 0
        for i in word:
            value = (value*10) + (ord(i)-97)
        return value
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """
        Determines if the sum of the numerical values of two given strings is equal to the numerical value of a third string.

        :param firstWord: A string representing the first word.
        :type firstWord: str
        :param secondWord: A string representing the second word.
        :type secondWord: str
        :param targetWord: A string representing the target word.
        :type targetWord: str
        :return: A boolean indicating if the sum of the numerical values of the first two words is equal to the numerical value of the target word.
        :rtype: bool
        """
        return self.get_the_value(firstWord)+self.get_the_value(secondWord) == \
                self.get_the_value(targetWord)