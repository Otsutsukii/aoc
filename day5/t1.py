

# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

from collections import defaultdict
import numpy as np


def solution1(data):
    # An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    # An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
    # For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

    # So, the horizontal and vertical lines from the above list would produce the following diagram:

    # .......1..
    # ..1....1..
    # ..1....1..
    # .......1..
    # .112111211
    # ..........
    # ..........
    # ..........
    # ..........
    # 222111....
    # In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

    # To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

    # Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
    # create a map of vents
    vent_map = defaultdict(int)
    vent_map2 = defaultdict(int)
    for line in data:
        x1,y1,x2,y2 = line[0][0],line[0][1],line[1][0],line[1][1]
        
        if x1 == x2:
            #vertical line
            for y in range(min(y1,y2),max(y1,y2)+1):
                vent_map[(x1,y)] += 1
                vent_map2[(x1,y)] += 1
        elif y1 == y2:
            #horizontal line
            for x in range(min(x1,x2),max(x1,x2)+1):
                vent_map[(x,y1)] += 1
                vent_map2[(x,y1)] += 1
            
            
    # count the number of points with 2 or more lines
    count = 0
    for key in vent_map:
        if vent_map[key] >= 2:
            count += 1
    return count


def solution2(data):
    # Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

    # Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

    # An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    # An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
    # Considering all lines from the above example would now produce the following diagram:

    # 1.1....11.
    # .111...2..
    # ..2.1.111.
    # ...1.2.2..
    # .112313211
    # ...1.2....
    # ..1...1...
    # .1.....1..
    # 1.......1.
    # 222111....
    # You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

    # Consider all of the lines. At how many points do at least two lines overlap?
    # create a map of vents
    vent_map = defaultdict(int)
    vent_map2 = defaultdict(int)
    for line in data:
        x1,y1,x2,y2 = line[0][0],line[0][1],line[1][0],line[1][1]
        
        if x1 == x2:
            #vertical line
            for y in range(min(y1,y2),max(y1,y2)+1):
                vent_map[(x1,y)] += 1
                vent_map2[(x1,y)] += 1
        elif y1 == y2:
            #horizontal line
            for x in range(min(x1,x2),max(x1,x2)+1):
                vent_map[(x,y1)] += 1
                vent_map2[(x,y1)] += 1
        # diagonal line
        else:
            # An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
            # An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
            # Considering all lines from the above example would now produce the following diagram:

            # 1.1....11.
            # .111...2..
            # ..2.1.111.
            # ...1.2.2..
            # .112313211
            # ...1.2....
            # ..1...1...
            # .1.....1..
            # 1.......1.
            # 222111....
            # get only the diagonal coordinates
            x_min = min(x1,x2)
            x_max = max(x1,x2)
            y_min = min(y1,y2)
            y_max = max(y1,y2)
            # get the slope
            slope = (y2-y1)/(x2-x1)
            # get the intercept
            intercept = y1 - slope*x1
            # get the coordinates of the diagonal line
            for x in range(x_min,x_max+1):
                y = int(slope*x + intercept)
                # vent_map[(x,y)] += 1
                vent_map2[(x,y)] += 1
            
            
            
    # count the number of points with 2 or more lines
    count = 0
    for key in vent_map2:
        if vent_map2[key] > 1:
            count += 1
    return count


def read_input(inputfile):
    # 0,9 -> 5,9
    # 8,0 -> 0,8s
    # 9,4 -> 3,4
    # 2,2 -> 2,1
    # 7,0 -> 7,4
    # 6,4 -> 2,0
    # 0,9 -> 2,9
    # 3,4 -> 1,4
    # 0,0 -> 8,8
    # 5,5 -> 8,2
    # Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:
    #read input file
    with open(inputfile) as f:
        data = f.readlines()
    #remove \n
    data = [x.strip() for x in data]
    #split into x1,y1,x2,y2
    data = [x.split('->') for x in data]
    #split into x1,y1,x2,y2
    data = [[x.split(',') for x in y] for y in data]
    #convert to int
    data = [[[int(x) for x in y] for y in z] for z in data]
    return data

if __name__ == '__main__':
    inputfile = 'input.txt'
    data = read_input(inputfile)
    print(data)
    print(solution1(data))
    print(solution2(data))