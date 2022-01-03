from turtle import dot,goto,penup, pendown, exitonclick
class Rectangle:
    def __init__(self,ll,ur):
        pass

    def draw(self):
        pass

class Point:
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y
    
    def draw(self) -> None:
        penup()
        goto(self.x, self.y)
        pendown()
        dot(10)
    
    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

pt = Point(10,10)
pt2 = Point()
rect = Rectangle(pt2, pt)
print(rect)
rect.draw()
print(f"pt1: {pt}, pt2: {pt2}")
pt.draw()
pt2.draw()
exitonclick()
