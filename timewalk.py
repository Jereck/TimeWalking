#NOTES
import datetime

now = datetime.datetime.now()
print (now)
datetime.timedelta(days=3)
print(now + datetime.timedelta(days=3))
print(now - datetime.timedelta(days=5))
print(now.date())
print(now.time())

hour = datetime.timedelta(hours=1)
workday = hour * 9
tomorrow = datetime.datetime.now().replace(hour= 9, minute=0) + datetime.timedelta(days=1)
print(tomorrow)
print (tomorrow + workday)

appointment = datetime.timedelta(minutes=45)
start = datetime.datetime(2017, 11, 1, 12, 45)
end = start + appointment
print (end)

now = datetime.datetime.now()
today = datetime.datetime.combine(datetime.date.today(), datetime.time())
print(today)
print(today.month)
print(today.day)
print(today.weekday())	#Monday is 0

print(now.timestamp())

######### DATE FORMATTING ######################
now = datetime.datetime.now()
print(now.strftime('%B %d'))
print(now.strftime('%m/%d/%Y'))

birthday = datetime.datetime.strptime('1989-07-25 08:18', '%Y-%m-%d %H:%M')
print(birthday)