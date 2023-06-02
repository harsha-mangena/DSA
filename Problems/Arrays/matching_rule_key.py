class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        """
        Counts the number of items in a list of lists that match a given rule.

        :param items: A list of lists containing the items to be searched.
        :type items: list[list[str]]
        :param ruleKey: The key to be used in the search. Valid keys are 'type', 'color', and 'name'.
        :type ruleKey: str
        :param ruleValue: The value to be searched for in the specified key.
        :type ruleValue: str
        :return: The number of items that match the given rule.
        :rtype: int
        """
        keys = {'type': 0, 'color': 1, 'name': 2}
        c = 0
        index = keys[ruleKey]
        for i in items:
            if i[index] == ruleValue:
                c += 1
        return c  