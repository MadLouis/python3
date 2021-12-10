class Point: # naming class should be use capital word
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print('move')
    
    def draw(self):
        print('draw')
    
    def louis(self):
        print('louis')


point = Point(10, 20)
point.x =11
print(point.x)

