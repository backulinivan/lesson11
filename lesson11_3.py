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
        

def massCentre(listOfPoints):  #для удобства считаем, что массы материальных точек равны
    xcm = 0
    ycm = 0
    for i in range(len(listOfPoints)):
        xcm += listOfPoints[i].x
        ycm += listOfPoints[i].y
    xcm = str(xcm)
    ycm = str(ycm)
    return(Point(xcm + ' ' + ycm))
    
points = [Point('13 4'), Point('2 5'), Point('7.34 3.14'), Point('1 1'), Point('7 8'), Point('10 5')]        
print(massCentre(points))            
