import datetime

import pytz

country = "Europe/Moscow"
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

print("***********                *******            ************** \n \n \n")
# for i in pytz.all_timezones:
#     print(i)
#
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])

for y in sorted(pytz.country_names):
    print("{}: {}".format(y, pytz.country_names[y]))
    if y in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[y]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}:   {}".format(zone, local_time))
    else:
        print("\t\tNo time zones defined")
