class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """
        Calculates the largest altitude reached by a fictional airplane that goes through a
        series of gains in altitude. The function takes a list of integers called gain as
        input, where gain[i] is the net gain in altitude between points i and i+1. The function
        returns the maximum altitude reached by the airplane during its journey. If the
        airplane never gains altitude, the function returns 0.

        :param gain: A list of integers representing the net gain in altitude between
                     consecutive points of the airplane's journey.
        :type gain: list[int]
        :return: An integer representing the maximum altitude reached by the airplane.
        :rtype: int
        """
        for i in range(1,len(gain)):
            gain[i] = gain[i]+gain[i-1]
        return max(0, max(gain))
        