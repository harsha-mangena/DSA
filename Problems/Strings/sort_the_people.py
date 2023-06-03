class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        """
        Sorts people by their height in descending order.

        :param names: A list of strings representing the names of the people.
        :type names: list[str]
        :param heights: A list of integers representing the heights of the people.
        :type heights: list[int]
        :return: A list of strings representing the sorted names of the people.
        :rtype: list[str]
        """
        height_people_map = []
        for i in range(len(heights)):
            height_people_map.append([heights[i], names[i]])
        height_people_map.sort(key=lambda x:x[0], reverse=True)

        return [x[1] for x in height_people_map]