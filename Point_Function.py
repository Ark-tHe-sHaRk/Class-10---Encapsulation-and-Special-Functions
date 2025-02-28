class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    #Method print points in the form (x, y)
    def __str__(self):
        return f"({self.x}, {self.y})"
    
#Object of class Point
P1 = Point(2, 3)
print(P1)