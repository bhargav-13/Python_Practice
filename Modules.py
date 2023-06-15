import time

# print(time.ctime(time.time()))

time_Obj = time.localtime()

local_time = time.strftime("%d / %B / %Y  %H:%M:%S", time_Obj )

print(local_time)