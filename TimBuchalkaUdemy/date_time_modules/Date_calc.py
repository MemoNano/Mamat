import random
import time
from time import perf_counter as my_timer

print(time.gmtime(0))
print(time.localtime(time.time()))
print(time.time())

print("************************  Time with Tuple     ************************")

time_here = time.localtime()
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)

print("*******  Game starts in this line **********")
input("Please enter your time here to start the Game: ")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to your time to stop the Game")

end_time = my_timer()
print("Started at: " + time.strftime("%X", time.localtime(start_time)))
print("Ended at: " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))
