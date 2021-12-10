class Point: # naming class should be use capital word
    def move(self):
        print('move')
    
    def draw(self):
        print('draw')
    
    def louis(self):
        print('louis')


point1 = Point()
point1.x =10
point1.y =20
print(point1.x)
point1.louis()
point2 = Point()
point2.draw()
