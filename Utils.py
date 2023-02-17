
import math
import matplotlib.pyplot as plt
from Point import Point
from Vector import Vector

# function to get the distance between two points
# point1: first point
# point2: second point
# return: distance between the two points
def get_distance(point1, point2):
    # get the x and y differences between the two points
    x_diff = point2.x - point1.x
    y_diff = point2.y - point1.y
    
    # return the distance between the two points
    return math.sqrt((x_diff * x_diff) + (y_diff * y_diff))

# function to normalize a vector
# vector: vector to normalize
# return: normalized vector
def normalize(vector):
    length = math.sqrt(vector.x * vector.x + vector.y * vector.y)
    vector.x = vector.x / length
    vector.y = vector.y / length
    return vector

# function to get magnitude of vector
# vector: vector to get magnitude of
# return: magnitude of the vector
def get_magnitude(vector):
    return math.sqrt((vector.x * vector.x) + (vector.y * vector.y))

# function to get angle between two vectors
# vector1: first vector
# vector2: second vector
# return: angle between the two vectors
def dot_product(vector1, vector2):
    return vector1.x * vector2.x + vector1.y * vector2.y

# function to get angle between two vectors
# vector1: first vector
# vector2: second vector
# return: angle between the two vectors
def get_angle(vector1, vector2):
    # get the dot product of the two vectors
    dot_prod = dot_product(vector1, vector2)

    
    # get the magnitude of the two vectors
    magnitude1 = get_magnitude(vector1)
    magnitude2 = get_magnitude(vector2)
    
    # get the angle between the two vectors
    # if magnitude1 or magnitude2 is 0, return 0
    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    angle = math.acos(dot_prod / (magnitude1 * magnitude2))
    
    # convert the angle to degrees
    angle = math.degrees(angle)

    # the direction of the angle is determined by the cross product of the two vectors
    # if the cross product is negative, the angle is negative
    cross_prod = vector1.x * vector2.y - vector1.y * vector2.x
    if cross_prod < 0:
        angle = -angle

    # return the angle between the two vectors
    return angle

# function get intersection of two lines
# line1: first line
# line2: second line
# return: intersection of the two lines POINT
def get_intersection(line1, line2):
    xdiff = Point(line1[0].x - line1[1].x, line2[0].x - line2[1].x)
    ydiff = Point(line1[0].y - line1[1].y, line2[0].y - line2[1].y)

    def det(a, b):
        return a.x * b.y - a.y * b.x

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = Point(det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return Point(x, y)

# function to return vector from point1 to point2
# point1: first point
# point2: second point
# return: vector from point1 to point2
def get_vector(point1, point2):
    # get the x and y differences between the two points
    x_diff = point2.x - point1.x
    y_diff = point2.y - point1.y
    
    # return the vector from point1 to point2
    return Vector(x_diff, y_diff)

# function that moves the point a distance of d, 90 degrees from the vector
# point: point to move
# vector: vector to move the point 90 degrees from
# d: distance to move the point
# return: new point
def perp_point(point, vector, d):
    # normalize the vector
    vector = normalize(vector)
    
    # get the perpendicular vector to the given vector using dot product
    perp_vector = Vector(-vector.y, vector.x) 

    #check vector and perp_vector are perpendicular
    if dot_product(vector, perp_vector) != 0:
        print("Error: Vectors are not perpendicular")
        return None
    # get the new point
    new_point = Point(point.x + (perp_vector.x * d), point.y + (perp_vector.y * d))
    
    # return the new point
    return new_point

# function will get proportion point 
# GetProportionPoint(PointF point, double segment, double length, double dx, double dy)
# point: point to get the proportion point from
# segment: segment to get the proportion point from
# length: length of the segment
# dx: x component of the vector
# dy: y component of the vector
# return: proportion point
def get_proportion_point(point, segment, length, dx, dy):
    # get the proportion of the segment
    proportion = segment / length

    # get the proportion point
    proportion_point = Point(point.x - (dx * proportion), point.y - (dy * proportion))

    # return the proportion point
    return proportion_point

#function will get cross product of two vectors
# vector1: first vector
# vector2: second vector
# return: cross product of the two vectors
def get_cross_product(vector1, vector2):
    #get the cross product of the two vectors
    cross_product = (vector1.x * vector2.y) - (vector1.y * vector2.x)

    #return the cross product of the two vectors
    return cross_product

# func that will get the length of a vector
# dx: x component of the vector
# dy: y component of the vector
# return: length of the vector
def get_length(dx: float, dy: float) -> float:
    return math.sqrt(dx*dx + dy*dy)

#function that will get the proportion point
# point: point to get the proportion point from
# segment: segment to get the proportion point from
# length: length of the segment
# dx: x component of the vector
# dy: y component of the vector
# return: proportion point
def get_proportion_point(point: Point, segment: float, length: float, dx: float, dy: float) -> Point:
    factor = segment / length
    return Point(point.x - dx * factor, point.y - dy * factor)

# function that will determine if a point is on the same side of a line as another point
# point1: first point
# point2: second point
# line_point1: first point of the line
# line_point2: second point of the line
# return: true if the point is on the same side of the line as the other point, false otherwise
def is_same_side(point1, point2, line_point1, line_point2):
    # get the cross product of the two vectors
    cross_product = get_cross_product(line_point2 - line_point1, point1 - line_point1)

    # get the cross product of the two vectors
    cross_product2 = get_cross_product(line_point2 - line_point1, point2 - line_point1)

    # check if the cross products have the same sign
    if(cross_product * cross_product2 >= 0):
        return True
    else:
        return False
    
# function that will determine if a point is inside a triangle
# point: point to check
# triangle_point1: first point of the triangle
# triangle_point2: second point of the triangle
# triangle_point3: third point of the triangle
# return: true if the point is inside the triangle, false otherwise
def is_point_in_triangle(point, triangle_point1, triangle_point2, triangle_point3):
    # check if the point is on the same side of the three lines
    if(is_same_side(point, triangle_point1, triangle_point2, triangle_point3) and is_same_side(point, triangle_point2, triangle_point1, triangle_point3) and is_same_side(point, triangle_point3, triangle_point1, triangle_point2)):
        return True
    else:
        return False
    
def draw_segments(points, bisectorPoint = None, old_points = None):
    # get the x and y coordinates of the points
    x = [point.x for point in points]
    y = [point.y for point in points]
    
    # draw the lines between the points
    plt.plot(x, y)
    
    # if there are old points
    if old_points is not None:
        # get the x and y coordinates of the old points
        x = [point.x for point in old_points]
        y = [point.y for point in old_points]
        
        # draw the lines in red
        plt.plot(x, y, 'r')

    if bisectorPoint is not None:
        # get the x and y coordinates of the old points
        x = [point.x for point in bisectorPoint]
        y = [point.y for point in bisectorPoint]
        
        # draw the point in blue
        plt.plot(x, y, 'bo')
    # show the plot
    plt.show()