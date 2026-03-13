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
    def __repr__(self):
        return self.__str__()
    def distance_origin(self):
        """
        Calculate the distance between point and origin
        :return: float, distance between point and origin
        """
        return (self.x_coordinate ** 2 + self.y_coordinate ** 2) ** 0.5
    def distance_to(self, point):
        """
        Calculate the distance between current point and another point
        :param point: the other point to calculate the distance to
        :return: float, distance between current point and another point
        """
        return((self.x_coordinate - point.x_coordinate) ** 2 +
               (self.y_coordinate - point.y_coordinate) ** 2) ** 0.5
    def __lt__(self, other):
        """
        Returns True if self is less than the other point
        :param other: the other point to compare against
        :return: True or False
        """
        return self.distance_origin() < other.distance_origin()

p1 = Point(1,2)
p2 = Point(3,4)
#p3 = Point("Bob", [1,2,3])
print(p1.x_coordinate, p1.y_coordinate)
print(p2.x_coordinate, p2.y_coordinate)
#print(p3.x_coordinate, p3.y_coordinate)

print(p1, p2)
print(f"{p2} distance to origin is {p2.distance_origin()}")
p3 = Point(12, 5)
print(f"{p3} distance to origin is {p3.distance_origin()}")
p1 = Point(6, 10)
p2 = Point(6, 15)
print(f"distance between {p1} and {p2} is: {p1.distance_to(p2)}")
p4 = Point(1,1)
points = [p1, p2, p3, p4]
print(points)
points.sort()
print(points)