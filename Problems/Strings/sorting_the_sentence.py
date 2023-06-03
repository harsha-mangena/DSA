class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        output = [None]*len(s)
        for word in s:
            index = int(word[-1])
            output[index-1] = word[:-1]
        return ' '.join(output)