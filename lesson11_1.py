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


A = Point(input())
B = Point(input())
print(A+B)
print(A-B)       
