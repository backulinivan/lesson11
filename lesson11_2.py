class Point:
    def __init__(self, coords = ''):
        arr = list(map(float, coords.split(' ')))
        self.x = arr[0]       #на вход координаты вида x y 
        self.y = arr[1]
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
    def __add__(self, other):
        sumx = str(self.x + other.x)
        sumy = str(self.y + other.y) 
        return Point(sumx + ' ' + sumy)
    def __sub__(self, other):
        sumx = str(self.x - other.x)
        sumy = str(self.y - other.y) 
        return Point(sumx + ' ' + sumy)
    def distance(self):
        return ((self.x)**2 + (self.y)**2)**0.5    
        
N = int(input())
maxDistance = 0
searchedPoint = Point('0 0')
for i in range(N):
    A = Point(input())
    if A.distance() > maxDistance:
        searchedPoint, maxDistance = A, A.distance()
        
print(searchedPoint)
print(maxDistance)

