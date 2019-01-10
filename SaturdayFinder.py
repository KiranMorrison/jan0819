'''
Function for finding the previous saturday
'''


import datetime
import time


while True:
	try:
		inputdate = input('Enter a date of your choice in the format YYYYMMDD >')
		if type(datetime.datetime.strptime(inputdate, '%Y%m%d')) is datetime.datetime:
			inputdatey = inputdate
			print('Well done! {} is a valid date'.format(inputdate))
			break
	except ValueError:
			print('{} is not a valid date you burke, read the question and try again'.format(inputdate))
print('Thank you, I remember it like it was yesterday...')
time.sleep(2)
print('wait for it...')
time.sleep(2)
print('wait for it.........')
time.sleep(3)
uglydate = datetime.datetime.strptime(inputdatey, '%Y%m%d')
prettydate = datetime.datetime.strftime(uglydate, '%A %Y-%m-%d')
dow = int(datetime.datetime.strftime(uglydate, '%w'))
dt = datetime.timedelta(days=dow+1)
sat = uglydate-dt
satstr = sat.strftime('%A %Y-%m-%d')
if dow == 6:
    print('Congrats, that was a Saturday')
else:
    print('If I remember correctly, the Saturday before {} was {}'.format(prettydate,satstr))
