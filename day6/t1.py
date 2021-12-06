import numpy as np
import pandas as pd
from aocd import get_data
# AOC_SESSION=53616c7465645f5fff3f1bb5ac32bd153673a7730f6c0fc99df849215b20a24c6ff09fa0a40510e01ec23e263c07f8c6
import numba
#import python timer
import time
# However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.

# Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.

# So, suppose you have a lanternfish with an internal timer value of 3:

# After one day, its internal timer would become 2.
# After another day, its internal timer would become 1.
# After another day, its internal timer would become 0.
# After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
# After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.
# A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

# Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:

# 3,4,3,1,2
# This list means that the first fish has an internal timer of 3, the second fish has an internal timer of 4, and so on until the fifth fish, which has an internal timer of 2. Simulating these fish over several days would proceed as follows:

# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8
# After  6 days: 4,5,4,2,3,4,5,6,6,7
# After  7 days: 3,4,3,1,2,3,4,5,5,6
# After  8 days: 2,3,2,0,1,2,3,4,4,5
# After  9 days: 1,2,1,6,0,1,2,3,3,4,8
# After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
# After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
# After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
# After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
# After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
# After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
# After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
# After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
# After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.

# In this example, after 18 days, there are a total of 26 fish. After 80 days, there would be a total of 5934.

# Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?


# use numba acceleration
# @numba.jit(nopython=True)
def solution1(data):
    # So, suppose you have a lanternfish with an internal timer value of 3:

    # After one day, its internal timer would become 2.
    # After another day, its internal timer would become 1.
    # After another day, its internal timer would become 0.
    # After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
    # After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.
    # A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

    # Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:

    # 3,4,3,1,2
    # This list means that the first fish has an internal timer of 3, the second fish has an internal timer of 4, and so on until the fifth fish, which has an internal timer of 2. Simulating these fish over several days would proceed as follows:

    # Initial state: 3,4,3,1,2
    # After  1 day:  2,3,2,0,1
    # After  2 days: 1,2,1,6,0,8
    # After  3 days: 0,1,0,5,6,7,8
    # After  4 days: 6,0,6,4,5,6,7,8,8
    # After  5 days: 5,6,5,3,4,5,6,7,7,8
    # After  6 days: 4,5,4,2,3,4,5,6,6,7
    # After  7 days: 3,4,3,1,2,3,4,5,5,6
    # After  8 days: 2,3,2,0,1,2,3,4,4,5
    # After  9 days: 1,2,1,6,0,1,2,3,3,4,8
    # After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
    # After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
    # After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
    # After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
    # After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
    # After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
    # After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
    # After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
    # After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
    # Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.

    # In this example, after 18 days, there are a total of 26 fish. After 80 days, there would be a total of 5934.

    # Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?
    
    timer = [x for x in data]
    days = 80
    # days = 256
    for i in range(days):
        for j in range(len(timer)):
            if timer[j] == 0:
                timer[j] = 6
                timer.append(8)
            else:
                timer[j] -= 1
    return len(timer)
    

from numba import njit
from numba.typed import List    
    
@numba.jit(nopython=True)    
def solution2(data):
#     Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?
# How many lanternfish would there be after 256 days?
    # use a counter from 0 to 8 
    count = np.zeros(9)
    for x in data:
        count[x] += 1
    days = 256
    for i in range(days):
        # rotate the counter
        tmp = count[0]
        count[0] = count[1]
        count[1] = count[2]
        count[2] = count[3]
        count[3] = count[4]
        count[4] = count[5]
        count[5] = count[6]
        count[6] = count[7] + tmp
        count[7] = count[8]
        count[8] = tmp
    # numba way to compute sum of array 
    return int(np.sum(count))


def solution3(data):
#     Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?
# How many lanternfish would there be after 256 days?
    # use a counter from 0 to 8 
    count = np.zeros(9)
    for x in data:
        count[x] += 1
    days = 256
    for i in range(days):
        # rotate the counter
        tmp = count[0]
        count[0] = count[1]
        count[1] = count[2]
        count[2] = count[3]
        count[3] = count[4]
        count[4] = count[5]
        count[5] = count[6]
        count[6] = count[7] + tmp
        count[7] = count[8]
        count[8] = tmp
    # numba way to compute sum of array 
    return int(np.sum(count))


def read_input(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
        data = [int(x) for x in data[0].split(',')]
    return data

if __name__ == '__main__':
    inputfile = 'input.txt'
    print(get_data(day=6, year=2021))
    print(type(get_data(day=6, year=2021)))
    data = read_input(inputfile)
    # print(data)
    data = data*10
    typed_a = List()
    [typed_a.append(x) for x in data]
    print(solution1(data))
    #record time 
    start = time.time()
    print(solution2(typed_a))
    end = time.time()
    print(end - start)
    
    start = time.time()
    print(solution3(data))
    end = time.time()   
    print(end - start)