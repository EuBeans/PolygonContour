

from Point import Point
from Vector import Vector
from PolygonContour import *

if __name__ == '__main__':

    # segment of points to contour around
    points = [Point(10, 12), Point(12, 6), Point(8, 8), Point(9, 4), Point(1, 10), Point(2, 2), Point(3,7), Point(0, 5), Point(12, 5)]
    #points = [Point(1, 6), Point(12, 5), Point(8, 9), Point(9, 4), Point(4, 10), Point(10, 7), Point(1, 3), Point(0, 0), Point(12, 4)]
    #points = [Point(-2, 1), Point(2, 4), Point(6, 1), Point(4, 2), Point(3, 3), Point(2, 2)]
    #points = [ Point(1.14, 10), Point(2, 2), Point(1, 5),Point(0, 0)]

    DISTANCE = 0.4
    RADIUS = 0.5
    # get the list of points that wraps around the list of points by the given distance
    result = generate_points(points, DISTANCE, RADIUS)
    # draw the list of points
    draw_segments(points,[], result)
