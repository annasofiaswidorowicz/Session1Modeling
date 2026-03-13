#OOP and classes
class Point:
    """
    Simple class to represent a point in 2D space
    """
    def __init__(self, x, y):
        """
        Consrtuctor for Point class
        :param x: coordinate of point
        :param y: cooridnate of point
        """
        self.x_coordinate = x #x is a class attribute
        self.y_coordinate = y
    def __str__(self):
        """
        String representation of Point class
        :return: string representation of Point class
        """
        return f"P<{self.x_coordinate},{self.y_coordinate}>"


p1 = Point(1,2)
p2 = Point(3,4)
#p3 = Point("Bob", [1,2,3])
print(p1.x_coordinate, p1.y_coordinate)
print(p2.x_coordinate, p2.y_coordinate)
#print(p3.x_coordinate, p3.y_coordinate)

print(p1, p2)
