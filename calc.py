"""
Sys args:

in file txt, out file txt, shift_sec

"""

import sys 

assert len(sys.argv) >= 3, "Must have both in and out file"

total_hour = 0
total_min = 0
total_sec = 0 

if (len(sys.argv) > 3):
    total_sec = int(sys.argv[3])

with open(sys.argv[1], "r") as in_f:
    with open(sys.argv[2], "w") as out_f:
        line = in_f.readline()
        while(line != ""):
            
            lst = line.strip().split(",")
            time_list = lst[0].split(":")
            title = lst[1].strip()
            total_hour += int(time_list[0])
            total_min += int(time_list[1])
            total_sec += int(time_list[2])

            total_min += total_sec // 60
            total_sec = total_sec % 60

            total_hour += total_min // 60 
            total_min = total_min % 60

            out_f.write("{}:{}:{},{}\n".format(total_hour, total_min, total_sec, title))

            line = in_f.readline()    

print("Total time: {} : {} : {}".format(total_hour, total_min, total_sec))

