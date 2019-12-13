import math


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return math.sqrt( (self.x - other.x) ** 2 + (self.y - other.y) ** 2 )

receiver = input().split(' ')

position = list()

for i in range(5):
    position.append(Coordinate(int(receiver[2 * i]), int(receiver[2 * i + 1]) ) )

positionLast = Coordinate(0, 0)
distanceSum = 0
while len(position) != 0:
    minLen = float('inf')
    record = 0
    for i in range(len(position)):
        distance = position[i] - positionLast
        if minLen > distance:
            minLen = distance
            record = i
    positionLast = position[record]
    distanceSum = distanceSum + minLen
    position.pop(record)
distanceSum = distanceSum + (positionLast - Coordinate(0,0))
print(distanceSum.)