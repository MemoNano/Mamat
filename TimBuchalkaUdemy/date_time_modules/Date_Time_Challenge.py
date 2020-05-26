"""
Write a small program to display information on the four clocks
 whose functions we have just looked at:
i.e. time(), perf_counter(), monotonic() and process_time().

Use the documentation for the get_clock_info() function
to work out how to call it for each of the clocks.
"""
import time
from time import localtime as local_time
from time import perf_counter as performance_count
from time import process_time as processor_time
from time import time as my_time

print(processor_time(), "--> process time")
print(performance_count(), "--> performance time")
print(my_time(), "Your machine local time")
time_lapce = local_time()
print("Year:", time_lapce[0], "  Month:", time_lapce[1], "  Day:", time_lapce[2], "  Hour:",
      time_lapce[3], "Minute:", time_lapce[4])

print("process()" + "\t", time.get_clock_info('process_time'))
