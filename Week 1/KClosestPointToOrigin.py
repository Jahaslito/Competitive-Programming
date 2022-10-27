class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        originX, originY = 0, 0
        pointsDistance = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            xDistanceSquared = (x - originX)** 2
            yDistanceSquared = (y - originY) ** 2
            distance = sqrt(xDistanceSquared + yDistanceSquared)
            pointsDistance.append((distance, points[i]))

        pointsDistance = sorted(pointsDistance)
        output = []
        for i in range(k):
            print(k)
            print(i)
            output.append(pointsDistance[i][1])

        return output
