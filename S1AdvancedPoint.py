from S1ColorPoint import ColorPoint

class AdvancedPoint(ColorPoint):
    #new class variables
    COLORS = ["red", "green", "blue", "yellow", "black", "white"]
    def __init__(self, x, y, color):
        #check the color
        if color not in self.COLORS:
            raise ValueError(f"Invalid color: need to be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color #_ makes it hidden (internal)

    @property #used to access the value now that it's hidden
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        if value not in self.COLORS:
            raise ValueError(f"Invalid color: need to be one of {self.COLORS}")
        self._color = value
    @classmethod
    def add_color(cls, color):
        cls.COLORS.append(color) #add new color to the list
    @staticmethod
    def distance_2_points(p1, p2):
        return((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

    @staticmethod #"factory" method because it allows to create from a dictionary
    def from_dict(d):
        x = d["x"]
        y = d["y"]
        color = d["color"]
        return AdvancedPoint(x, y, color)

point_dict = {"x": 1, "y": 2, "color": "red"}
p0 = AdvancedPoint.from_dict({"x": 1, "y": 2, "color": "red"})
print(p0)
p1 = AdvancedPoint(1, 2, "red")
print(p1)
p2 = AdvancedPoint(3, 4, "white")
print(p2)
#p1.x = 7
#print(p1.x)
#call class methods via class name instead of the instance name
AdvancedPoint.add_color("coral")
p3 = AdvancedPoint(1, 2, "coral")
print(p3)
print(AdvancedPoint.distance_2_points(p1, p3))





