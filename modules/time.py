import time

print(time.ctime())           # convert seconds since epoch to a string representing local time.
print(time.time())            # Returns the current time in seconds since the epoch.
print(time.ctime(time.time())) # Returns the current time in a readable format.

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) # Returns the current time in a readable format.
time.gmtime()                 # Returns the current time in UTC time.
time.localtime()              # Returns the current time in local time.
