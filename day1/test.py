
# For example, suppose you had the following report:
# 199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263
# This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

# The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

# To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

# 199 (N/A - no previous measurement)
# 200 (increased)
# 208 (increased)
# 210 (increased)
# 200 (decreased)
# 207 (increased)
# 240 (increased)
# 269 (increased)
# 260 (decreased)
# 263 (increased)
# In this example, there are 7 measurements that are larger than the previous measurement.

# How many measurements are larger than the previous measurement?

# input list of depths

# read the inputfile and store the depths in a list
def read_input(inputfile):
    with open(inputfile, 'r') as f:
        depths = f.read().splitlines()
    return depths

def solution(depths):
    # initialize a counter
    count = 0
    # initialize a previous depth
    prev_depth = depths[0]
    # iterate through the depthss
    for depth in depths:
        # if the depth is larger than the previous depth, increment the counter
        if int(depth) > prev_depth:
            count += 1
        # set the previous depth to the current depth
        prev_depth = int(depth)
    return count

if __name__ == '__main__':
    inputfile = 'input.txt'
    depths = read_input(inputfile)
    print(solution(depths))