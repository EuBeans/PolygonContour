##!/bin/python

import math
import matplotlib.pyplot as plt
from Point import Point
from Vector import Vector
from Utils import *


#TODO Figure out the order of generating points, it seems to be backwards for some angles. This will lower the complexity from O(n^2) to O(n)

# function will generate the contour of the given polygon only on one side, this will be the skeleton of the contour
# points: list of points that make up the polygon
# distance: distance to move the contour from the polygon
# return: list of points that make up the contour
# complexity: O(n)
def generate_contour(points, distance):
    # get the number of points in the list
    num_points = len(points)
    
    # create a list to hold the result
    result = []
   
    # for each point in the list
    for i in range(num_points):
        current_point = points[i]
        next_point = points[(i + 1) % num_points]
        previous_point = points[(i - 1) % num_points]

        #if the point is the first point
        if i == 0:
            #get vector from current point to next point
            vector = Point(next_point.x - current_point.x, next_point.y - current_point.y)
            #get a point perpendicular to the vector from the current point by the distance given 
            new_point = perp_point(current_point, vector, distance)
            # add the new point to the result
            result.append(new_point)

        #if the point is the last point
        elif i == num_points - 1:
            #get vector from current point to previous point
            vector = Point(current_point.x - previous_point.x, current_point.y - previous_point.y)
            #get a point perpendicular to the vector from the current point by the distance given 
            new_point = perp_point(current_point, vector, distance)
            # add the new point to the result
            result.append(new_point)
        
        else: 
            # get the vector from the previous point to the current point
            vector1 = Vector(current_point.x - previous_point.x, current_point.y - previous_point.y)    
            # get the vector from the current point to the next point
            vector2 = Vector(next_point.x - current_point.x, next_point.y - current_point.y)

            vector1_perp_point = perp_point(current_point, vector1, distance)
            vector2_perp_point = perp_point(current_point, vector2, distance)

            result.append(vector1_perp_point)
            result.append(vector2_perp_point)
    
    return result


#function will calculate and generate a list of points for the rounded corners of a convex corner
# point1: first point of the corner
# point2: second point of the corner
# angular_point: third point of the corner
# radius: radius of the rounded corner
# return: list of points that make up the rounded corner
# Complexity O(1), but since we are using list.reverse() the complexity is O(n)
# https://stackoverflow.com/questions/24771828/how-to-calculate-rounded-corners-for-a-polygon
# https://gorillasun.de/blog/an-algorithm-for-polygons-with-rounded-corners
def generate_rounded_corner(angular_point: Point, p1: Point, p2: Point, radius: float):
# Vector 1
    dx1 = angular_point.x - p1.x
    dy1 = angular_point.y - p1.y

    # Vector 2
    dx2 = angular_point.x - p2.x
    dy2 = angular_point.y - p2.y

    # Angle between vector 1 and vector 2 divided by 2
    angle = (math.atan2(dy1, dx1) - math.atan2(dy2, dx2)) / 2
    angleD = math.degrees(angle)

    # The length of segment between angular point and the
    # points of intersection with the circle of a given radius
    tan = abs(math.tan(angle))
    if(angle == 0):
        return []
    segment = radius / tan


    # Check the segment
    length1 = get_length(dx1, dy1)
    length2 = get_length(dx2, dy2)

    length = min(length1, length2)

    if segment > length:
        segment = length
        radius = length * tan

    # Points of intersection are calculated by the proportion between
    # the coordinates of the vector, length of vector and the length of the segment.
    p1_cross = get_proportion_point(angular_point, segment, length1, dx1, dy1)
    p2_cross = get_proportion_point(angular_point, segment, length2, dx2, dy2)

    # Calculation of the coordinates of the circle
    # center by the addition of angular vectors.
    dx = angular_point.x * 2 - p1_cross.x - p2_cross.x
    dy = angular_point.y * 2 - p1_cross.y - p2_cross.y

    l = get_length(dx, dy)
    d = get_length(segment, radius)

    circle_point = get_proportion_point(angular_point, d, l, dx, dy)

    # StartAngle and EndAngle of arc
    start_angle = math.atan2(p1_cross.y - circle_point.y, p1_cross.x - circle_point.x)
    end_angle = math.atan2(p2_cross.y - circle_point.y, p2_cross.x - circle_point.x)
    start_angleD = math.degrees(start_angle)
    end_angleD = math.degrees(end_angle)
    # Sweep angle
    sweep_angle = end_angle - start_angle

    # Some additional checks
    if sweep_angle < 0:
        start_angle = end_angle
        sweep_angle = -sweep_angle
    flag = False
    if sweep_angle > math.pi:
        #This flag is used to reverse the order of the rounded corner list of points. This is needed because the points are generated in a clockwise direction, but the points need to be generated in a counter-clockwise direction. when the sweep angle is greater than 180 degrees
        flag = True
        sweep_angle = -(math.pi * 2 - sweep_angle)


    #normalize dx1 and dy1
    v1 = Vector(dx1, dy1)
    v1.normalize()
    v2 = Vector(dx2, dy2)
    v2.normalize()

    sinA = v1.x * v2.y - v1.y * v2.x
    sinA90 = v1.x * v2.x - v1.y * -v2.y
    angle2 = math.asin(-1 if sinA < -1  else 1 if sinA > 1  else sinA)
    
    radDirection = 1
    drawDirection = False
    if (sinA90 < 0):
        if (angle2 < 0):
            angle2 = math.pi - angle2
        else:
            angle2 = math.pi - angle2
            radDirection = -1
            drawDirection = True
        
    else:
        if (angle2 > 0):
            radDirection = -1
            drawDirection = True
        


    degree_factor = 30
    points_count = int(abs(sweep_angle * degree_factor))
    sign = int(math.copysign(1, sweep_angle))

    points = []

    for i in range(points_count):
        point_x = circle_point.x + math.cos(start_angle + sign * float(i) / degree_factor) * radius 
        point_y = circle_point.y + math.sin(start_angle + sign * float(i) / degree_factor) * radius
        points.append(Point(point_x, point_y))
    #draw_segments([p1,angular_point,p2], [Point(circle_point.x,circle_point.y)],points)

    points.reverse() if flag else points
    return points

# function will add rounded corner to intersection that are outside of the triangle
# outer_points: list of points that make up the contour
# original_points: list of points that make up the original frame
# radius: radius of the rounded corner between 0.1 and 1
# return: list of points that make up the contour
# Complexity O(n) but since we are using list.reverse() it is O(n^2)
def add_rounded_corner(outer_points, original_points, radius):
    # get the number of points in the list
    num_points = len(outer_points)
    num_original_points = len(original_points)

    # create a list to hold the result
    result = []
    current_point = outer_points[0]
    previous_intersection = None
    i = 0
    j = 0 
    while(i < num_points ):
        
        if(previous_intersection):
            previous_point = previous_intersection
        else: 
            previous_point = outer_points[(i - 1) % num_points]
        
        current_point = outer_points[i]
        next_point = outer_points[(i + 1) % num_points]
        next_next_point = outer_points[(i + 2) % num_points]

        frame_previous_point = original_points[(j - 1) % num_original_points]
        frame_current_point = original_points[j % num_original_points]
        frame_next_point = original_points[(j + 1) % num_original_points]

        if(is_point_in_triangle(current_point,frame_previous_point, frame_current_point, frame_next_point)):
            intersection = get_intersection([previous_point, current_point],[current_point,next_point])
        else:
            intersection = get_intersection([previous_point, current_point],[next_point, next_next_point])
        vector1 = Vector(current_point.x - previous_point.x, current_point.y - previous_point.y)
        vector2 = Vector(next_point.x - current_point.x, next_point.y - current_point.y)
        angle = get_angle(vector1, vector2)

        if(i == 0):
            result.append(current_point)
        elif(i == num_points - 1):
            result.append(current_point)
        else:
            if(intersection):
                #if not in triangle
                if(not is_point_in_triangle(intersection, frame_previous_point, frame_current_point, frame_next_point)):
                    result.append(current_point)
                    roundedCornerPoints = generate_rounded_corner(intersection,current_point, next_point, radius)
                    
                    previous_intersection = None
                    i+= 1

                    if(angle < 0):
                        roundedCornerPoints.reverse()
                    
                    result.extend(roundedCornerPoints)
                else:
                    result.append(current_point)
                    previous_intersection = None
        i += 1
        j += 1
    return result


# function will go through the newly generated points and find the intersection of the lines, remove the extra points and add the intersection points
# outer_points: list of points that make up the contour
# original_points: list of points that make up the original frame
# radius: radius of the rounded corner between 0.1 and 1
# return: list of points that make up the contour
# Complexity O(n)
def fix_intersection_point(outer_points, original_points):
    # get the number of points in the list
    num_points = len(outer_points)
    num_original_points = len(original_points)

    # create a list to hold the result
    result = []
    current_point = outer_points[0]
    previous_intersection = None
    i = 0
    j = 0 
    while(i < num_points ):
        
        if(previous_intersection):
            previous_point = previous_intersection
        else: 
            previous_point = outer_points[(i - 1) % num_points]
        
        current_point = outer_points[i]
        next_point = outer_points[(i + 1) % num_points]
        next_next_point = outer_points[(i + 2) % num_points]

        intersection = get_intersection([previous_point, current_point],[next_point, next_next_point])

        frame_previous_point = original_points[(j - 1) % num_original_points]
        frame_current_point = original_points[j % num_original_points]
        frame_next_point = original_points[(j + 1) % num_original_points]

        if(i == 0):
            result.append(current_point)

        elif(i == num_points - 1):
            result.append(current_point)
        else:
            if(intersection):
                if(is_point_in_triangle(intersection, frame_previous_point, frame_current_point, frame_next_point)):
                    result.append(intersection)
                    previous_intersection = intersection
                    
                else:
                    result.append(current_point)
                    result.append(next_point)
                    previous_intersection = None
                i+=1
        i+=1
        j+=1
    result.append(outer_points[num_points - 1])
    return result

# This function will generate a list of points that wraps around the given polygon by the given distance as buffer\
# points: list of points that make up the polygon
# distance: distance of the buffer between 0.1 and 0.4
# radius: radius of the rounded corner between 0.1 and 1
# return: list of points that make up the contour
# Complexity O(n)
def generate_points(points, distance,radius):
    # create a list to hold the result

    if distance > 0.4 or distance < 0:
        raise ValueError("Distance must be between 0.1 and 0.4")
    
    if radius > 1 or radius < 0:
        raise ValueError("Radius must be between 0.1 and 1")
    
    result = []
    #generate the outer contour
    outer_contour = generate_contour(points, distance)
    outer_contour = fix_intersection_point(outer_contour,points)

    outer_contour = add_rounded_corner(outer_contour, points, radius)


    result.extend(outer_contour)

    inner_contour = generate_contour(points, -distance)
    inner_contour = fix_intersection_point(inner_contour,points)

    inner_contour = add_rounded_corner(inner_contour, points, radius)

    inner_contour.reverse()
    result.extend(inner_contour)
    #close of the contour
    result.append(result[0])

    return result
