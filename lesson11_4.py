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
        

def maxPerimeter(arr):
    maxPer = 0
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            for k in range(2, len(arr)):
                per = dist(arr[i], arr[j]) + dist(arr[i], arr[k]) + dist(arr[k], arr[j])
                if per > maxPer:
                    maxPer = per
    return maxPer                    

def dist(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5



points = [Point('13 4'), Point('2 5'), Point('7.34 3.14'), Point('1 1'), Point('7 8'), Point('10 5')]        
print(maxPerimeter(points))          
