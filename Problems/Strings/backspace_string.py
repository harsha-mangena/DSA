class Solution():
    def backspaceCompare(self, S, T):
        """
        Given two strings S and T, this function backspaceCompares them and returns a boolean. 

        :param S: A string representing the first string.
        :type S: str
        :param T: A string representing the second string.
        :type T: str
        :return: A boolean representing if the two strings are equal after processing.
        :rtype: bool
        """
        def _process_string(S):
            """
            Returns a string with all characters except '#' in the input string S. This function takes
            a string as an argument S and returns a string. The returned string has all the characters 
            except the '#' characters in the input string S. If the '#' character is found in the string, 
            the previous character is removed from the list of characters to be returned. If the '#' 
            character is the first character in the string S, it is ignored. If the string S is empty, 
            an empty string is returned.
            """
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return _process_string(S) == _process_string(T)