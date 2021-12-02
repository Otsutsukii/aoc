from shutil import copyfile
import os 
# create directory name from day 4 to 25 
# copy all files from directory day 3 to directory day 4 to 25
for i in range(4, 26):
    # create directory name from day 4 to 25 
    dir_name = "day" + str(i)
    # create directory if it does not exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    # copy all files from directory day 3 to directory day 4 to 25
    for file in os.listdir("day3"):
        copyfile("day3/" + file, dir_name + "/" + file)
