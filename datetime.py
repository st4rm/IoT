import time
import datetime

# From String to datetime object
#date_string = '2017-11-14 21:22:23'
#datetime.datetime.strptime('date_string', '%Y-%m-%d %H:%M:%S')
#print(date_string)

# From Timestamp to datetime
timestamp = time.time()
print('time stamp is ', timestamp)
datetimeobj = datetime.datetime.fromtimestamp(timestamp/1000)
print(datetimeobj)

# From datetime to timestamp
timestamp = time.mktime(datetimeobj.timetuple())
print(timestamp)

