# PolygonContour
#### algorithm for implementing the edge effect offset

The code is a program that takes a list of points and generates a list of points that wraps around the list of points by the given distance. The code is written in a way that it can be used as a module in other programs. 

## Features

- Generates a List of points that will contour your segments
- Alter the distance of the padding between the segments and the contour
- Alter the radius of sharp angles


## Explanation 
First, for each point in the list, we will add a contour point that is perpendicular to the line between the current point and the next point at a certain distance.

Second, we will go through the newly generated points and find the intersection of the lines, remove the extra points and add the intersection points. This is only done if the intersection point is in the triangle formed by the current point and the next point and the previous point.

Third, we will go through the newly generated points and find the intersection of the lines, (only for the intersection that is outside the triangle). For these intersections, we will generate a list of points that make up the rounded corner. The way we do this is by finding the incenter of the incircle of the triangle formed by the current point, the next point and the intersection point.

We will then generate a list of points that make up the arc of the circle that is tangent to the line between the current point and the next point and the line between the current point and the intersection point. We will then add the list of points to the result list.

## Issue That needs resolving
One issue that needs to be fixed is the order of which we generate the rounded corner (clockwise or counter clockwise). This is done by finding the angle between the two lines. However there are some cases where the order is not correct. 

## Few Examples

![Segments with Complex Angles](/img/Example1.png)


![Segments with Complex Angles](/img/Example2.png)


## Sources
<https://mcmains.me.berkeley.edu/pubs/DAC05OffsetPolygon.pdf>
<https://stackoverflow.com/questions/24771828/how-to-calculate-rounded-corners-for-a-polygon>
<https://gorillasun.de/blog/an-algorithm-for-polygons-with-rounded-corners>
<https://dl.acm.org/doi/pdf/10.1145/129902.129906>
<https://doc.cgal.org/Manual/3.2/doc_html/cgal_manual/Straight_skeleton_2/Chapter_main.html#Section_16.3>
<https://stackoverflow.com/questions/1109536/an-algorithm-for-inflating-deflating-offsetting-buffering-polygons>

