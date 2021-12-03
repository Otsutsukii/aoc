# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010
# Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

# The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

# The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

# So, the gamma rate is the binary number 10110, or 22 in decimal.

# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
from collections import Counter


def calculate_gamma_rate(data):
    gamma_rate = []
    epsilon_rate = []
    #for the length of each line in the data
    # for all the bits, calculate the occurences of each bit
    # for each bit, calculate the most common bit

    for i in range(len(data[0])):
        common = Counter([x[i] for x in data]).most_common(1)[0][0]
        epsilon_rate.append(Counter([x[i] for x in data]).most_common(2)[1][0])

        gamma_rate.append(common)
        print(common)
    return int(''.join(gamma_rate),2), int(''.join(epsilon_rate),2), int(''.join(gamma_rate),2)*int(''.join(epsilon_rate),2)

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
# Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:

# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
# For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

# Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
# Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
# In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
# In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
# In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
# As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
# Then, to determine the CO2 scrubber rating value from the same example above:

# Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
# Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
# In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
# As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
# Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

# Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)


def get_oxygen_generator_rating(data):
    # get the oxygen generator rating
    # for example : 
    # Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
    # Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
    # In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
    # In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
    # In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
    # As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
    # Then, to determine the CO2 scrubber rating value from the same example above:
    length = len(data[0])
    data2 = data
    for i in range(length):
        # get the most common bit
                    
        if len(data) == 1:
            oxygen = int(''.join(data[0]),2)
            break
        common = Counter([x[i] for x in data])
        if common.most_common(1)[0][1] > common.most_common(2)[1][1]:
            rating = common.most_common(1)[0][0]
        elif common.most_common(1)[0][1] < common.most_common(2)[1][1]:
            rating = common.most_common(2)[1][0]
        else:
            rating = '1'
        data = [x for x in data if x[i] == rating]
    # do the same thing for the CO2 scrubber rating
    for i in range(length):
        # get the least common bit
        if len(data2) == 1:
            CO2 = int(''.join(data2[0]),2)
            break
        common = Counter([x[i] for x in data2])
        if common.most_common(1)[0][1] > common.most_common(2)[1][1]:
            rating = common.most_common(2)[1][0]
        elif common.most_common(1)[0][1] < common.most_common(2)[1][1]:
            rating = common.most_common(1)[0][0]
        else:
            rating = '0'
        data2 = [x for x in data2 if x[i] == rating]
    return int(''.join(data[0]),2)*int(''.join(data2[0]),2)


def read_input(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    return data

if __name__ == '__main__':
    inputfile = 'input.txt'
    data = read_input(inputfile)
    print(calculate_gamma_rate(data))
    # print(solution2(data))
    print(get_oxygen_generator_rating(data))