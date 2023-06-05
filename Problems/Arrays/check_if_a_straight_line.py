class Solution:
      def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        """
        Determines if a set of coordinates form a straight line.

        Args:
            coordinates (list[list[int]]): A list of coordinates, where each coordinate is a list containing
                two integers representing the x and y coordinates respectively.

        Returns:
            bool: True if the given coordinates form a straight line, False otherwise.
        """
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True
                