# https://stackoverflow.com/questions/40672243/start-and-end-time-of-yesterday-in-time-stamp-python

# import time
# startDay = time.strftime('%Y-%m-%d 00:00:00')
# endDay   =time.strftime('%Y-%m-%d 23:59:59')

# def datetime_timestamp(dt):
#     time.strptime(dt, '%Y-%m-%d %H:%M:%S')
#     s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
#     return int(s)

# print(startDay)
# print(endDay)

# print("resetTime")

# print(datetime_timestamp(startDay))
# print(time.time())


import datetime
base = datetime.datetime.fromtimestamp(0)
nextReset = datetime.datetime.now().replace(hour=0,minute=0,second=0, microsecond=0)
nextReset = nextReset + datetime.timedelta(days= +1, seconds= -1)
nextResetUnix = int((nextReset - base).total_seconds())
print(nextReset)
print(nextResetUnix)

today = datetime.datetime.now()
todayUnix = int((today - base).total_seconds())
print(today)
print(todayUnix)

if todayUnix >= nextResetUnix:
	print('reset time')
else:
	print('lanjut boss')

# midnight2 = datetime.datetime.now().replace(hour=0,minute=0,second=0, microsecond=0)
# midnight2 = midnight2 - datetime.timedelta(seconds= +1)
# midnight1 = midnight2 - datetime.timedelta(days= +1, seconds= -1)
# yesterday = (midnight1 - base).total_seconds()
# thismorning = (midnight2 - base).total_seconds()
# print( midnight1,"timestamp",int(yesterday) )
# print( midnight2,"timestamp",int(thismorning) )
# print( "Seconds elapsed",thismorning - yesterday )