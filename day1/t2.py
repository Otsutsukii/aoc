# Consider sums of a three-measurement sliding window. Again considering the above example:

# 199  A      
# 200  A B    
# 208  A B C  
# 210    B C D
# 200  E   C D
# 207  E F   D
# 240  E F G  
# 269    F G H
# 260      G H
# 263        H
# Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

# Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

# In the above example, the sum of each three-measurement window is as follows:

# A: 607 (N/A - no previous sum)
# B: 618 (increased)
# C: 618 (no change)
# D: 617 (decreased)
# E: 647 (increased)
# F: 716 (increased)
# G: 769 (increased)
# H: 792 (increased)
# In this example, there are 5 sums that are larger than the previous sum.

# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

def solution(depths):
    # Initialize the sum of the first three-measurement window
    sum_of_measurements = int(depths[0]) + int(depths[1]) + int(depths[2])
    # Initialize the number of larger sums
    num_of_larger_sums = 0
    prev_sum = sum_of_measurements
    for i in range(3, len(depths)):
        # Get the current depth
        depth = int(depths[i]) + int(depths[i-1]) + int(depths[i-2])
        # Get the previous sum of the three-measurement window
        # prev_sum = sum_of_measurements
        # Update the sum of the three-measurement window
        sum_of_measurements = depth
        # Compare the sum of the three-measurement window with the previous sum
        if sum_of_measurements > prev_sum:
            num_of_larger_sums += 1
        prev_sum = int(depths[i]) + int(depths[i-1]) + int(depths[i-2])
    return num_of_larger_sums




def read_input(inputfile):
    with open(inputfile, 'r') as f:
        depths = f.read().splitlines()
    return depths



if __name__ == '__main__':
    inputfile = 'input2.txt'
    depths = read_input(inputfile)
    print(solution(depths))