from datetime import datetime,date,time as time2,timedelta
import time

#'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo'
print(dir(datetime))


print(date.today())
print(dir(time2))
print(time2(9,8))

ds = "2018-08-09 14:36:23"
ds_t = datetime.strptime(ds,"%Y-%m-%d %H:%M:%S")
print(ds_t.time())

print(time.time())

n = datetime.now()
print(n.strftime("%M"))

n_next = n + timedelta(days=5,hours=4)
print(n_next)

d1 = datetime(2018,10,15)
d2 = datetime(2018,10,16)

print(d2 > d1)

a = (x for x in range(8))
print(len(a))