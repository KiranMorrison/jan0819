import time
import random
from random import randint

print('\n' * 100)
print('\n\n[-Space Adventure by Kiran]')
print('\n\n\n------------------------')
print('        SPACE MARMALADE')
print('------------------------')
print('\n53.456.234 : krab inc.')
time.sleep(1)
print('\nInitialising defrost sequence...')
time.sleep(1)
print('\nWaking human subject 53...')
time.sleep(1)
print('....')
time.sleep(1)
print('Taking a leak')
time.sleep(1)
print('Your gun holster is empty...')
time.sleep(1)
print('Your shoes are missing...')
time.sleep(1)
print('\nYour pockets are full of secrets...')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
print('\nHuman is awake.')
time.sleep(1)
print('''\n\nYou are human subject #53. You are here to solve
the riddle of the marmalade. 53 others have failed before you,
not 52 like you're thinking but 53, because we started counting
at 0 you clever cloggs. Your mission, whether or not you choose
to accept it, is to navigate the six doors of destiny and escape
the devilish trap, solving the riddle of the marmalade in the 
process. If you fail you will die and you'll have to restart the
program, unlucky. You are sleepy from having been frozen for a
bit, but I hid your gun and stole your shoes... Good luck!''')

def start(inventory):
	print('\n----------')
	print('\nHuman53 mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('\n[-MAIN HALL-]')
	print('\n1.) Door 1 - Alpha')
	print('2.) Door 2 - Beta')
	print('3.) Door 3 - Gamma')
	print('4.) Door 4 - Delta')
	print('5.) Door 5 - Special secret room')
	print('6.) Door 6 - Do not disturb\n')
	
	cmdlist = ['1', '2', '3', '4', '5', '6',]
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		security(inventory)
	elif cmd == '2':
		if 'droid hack' in inventory:
			print('\n- Door 2 - MAINTENANCE LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			maintenance(inventory)
	elif cmd == '3':
		cargo_hold(inventory)
	elif cmd == '4':
		if 'laser' in inventory:
			print('\n- door 4 - DROID HANGAR LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			droid_hangar(inventory)
	elif cmd == '5':
		shuttle_control(inventory)
	elif cmd == '6':
		if 'motion tracker' in inventory:
			print('\n- door 6 - OBSERVATION LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			observation(inventory)
		
def maintenance(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nThis is the maintenance door and it appears deserted. 
You can see a terminated crew droid, it has sustained
severe laser fire.''')
	print('\n[-MAINTENANCE-]\n')
	print('1.) 716 Crew Droid')
	print('2.) Return to Main Elevator\n')
	
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	if cmd == '1':
		crew_droid(inventory)
	elif cmd == '2':
		start(inventory)
		
def crew_droid(inventory, items=['droid hack']):
	print('\n----------')
	print('''\n716 has a droid hack program and it's connection
outlet is still intact. You can connect to this droid with service
port and download the program.''')
	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
			print('\n\n1.) Exit.')
	cmdlist = ['service port', '1']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('droid hack')
			items = ['droid hack']
			print('\nservice port connected.')
			time.sleep(1)
			print('accessing file..')
			time.sleep(1)
			print('downloading..')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\ndownload complete.')
			print('\nYou have the droid hack program and return')
			print('to the Main Elevator.')
			time.sleep(2)
			start(inventory)
	elif cmd == '1':
			maintenance(inventory)
	else:
		print('\n error. invalid command-')
	
def cargo_hold(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nYou enter the Cargo Hold, two Enemy Combat droids
unload a barrage of laser fire at you. Their fire is very accurate
and you take a direct hit in your main CPU.''')
	print('\n[-CARGO HOLD - AIRLOCK-]')
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('\nshutdown imminent...')
	time.sleep(1)
	print('CTRL866 offline.')
	time.sleep(1)
	print('Droid terminated.')
	print('\nGAME OVER\n')
	exit(0)
	
def droid_hangar(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nThe Droid Hangar is filled with debri. There
is laser scoring everywhere and all droids are terminated.
In the corner there is one inactive repair droid still in his security
cylinder. You can initialise the droid to repair your laser but you will 
require a 3 digit access code.\n''')
	print('[-DROID HANGAR-]')
	print('\n1.) Repair Droid 3 digit code')
	print('2.) Return to Main Elevator')
	
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		access_code(inventory)
	elif cmd == '2':
		start(inventory)
		
def access_code(inventory):
	code = '%d%d%d' % (randint(0,9), randint(0,9), randint(0,9))
	guess = input('\n[KEYPAD]> ')
	guesses = 0
	
	while guess != code and guess != 'yu8xxj3' and guesses <4:
		print('\n* ACCESS - DENIED *')
		guesses += 1
		guess = input('\n[KEYPAD]> ')
		
	if guess == code or guess == 'yu8xxj3':
		repair_droid(inventory)
	else:
		print('\n....')
		time.sleep(1)
		print('\n....')
		time.sleep(1)
		print('\nKEYPAD - LOCKED')
		time.sleep(1)
		print('\ncode randomizing..')
		time.sleep(1)
		print('\nKEYPAD - OPEN')
		time.sleep(1)
		droid_hangar(inventory)
		
def repair_droid(inventory, items=['laser']):
	print('\n\n----------')
	print('\nREP323 boot sequence....')
	time.sleep(1)
	print('Initalizing Repair Droid 323....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('Repair Droid Active.')
	time.sleep(1)
	print('''\nThe Repair droid is now active. You MUST connect to
this droid with service port to repair laser.''')

	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
	cmdlist = ['service port']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('laser')
			items = ['laser']
			print('\nservice port connected.')
			time.sleep(1)
			print('Repairing Laser...')
			time.sleep(1)
			print('Auto alignment...')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\nLASER ONLINE.')
			print('''\nYour laser is now online. You de-activate the Repair
Droid and return to the Main Elevator.''')
			time.sleep(2)
			start(inventory)
	else:
		print('\n error. invalid command-')
		
def security(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nYou are on the Security door. This is where all
surveillance aboard the shuttle is done. Sentry droid 343 has been
terminated. You MUST access the Sentry droid's logs but you
will have to hack the data recorder.\n''') 
	print('[-SECURITY-]\n')
	print('1.) View Surveillance monitors on other doors')
	print('2.) Hack Sentry droid 343')
	print('3.) Return to main elevator')
	
	cmdlist =['1', '2', '3']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		print('\n----------')
		print('\nBooting Monitors....')
		time.sleep(1)
		print('....')
		time.sleep(1)
		print('...')
		time.sleep(1)
		print('Monitors active.')
		time.sleep(1)
		print('\n[-SURVEILLANCE FEED-]')
		print('''\n-The Hangar monitor is offline you have no live feed.
\n-In the Cargo hold there are two Enemy Combat droids patroling.
\n-The Maintenance door looks clear except for a few terminated droids.
\n-An Elite Enemy Command droid is posted on the Shuttle Control door.
\n-Observation shows a Enemy Sentry droid.''')
		time.sleep(2)
		security(inventory)
		
	elif cmd == '2':
		if 'droid hack' in inventory:
			print('\nloading droid hack....')
			time.sleep(2)
			print('....')
			time.sleep(2)
			print('10000101010101010101010' * 1000)
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('Accessing encrypted files...')
			time.sleep(2)
			print('Decrypting....')
			time.sleep(2)
			print('\n\n[-SEN343 LOG-]')
			time.sleep(1)
			print('\n\nDAILY OVER-RIDE CODES- HANGAR DROIDS')
			time.sleep(1)
			print('\n\n-Combat Droids - szb41ee')
			time.sleep(1)
			print('\n\n-Sentry Droids - qr66mop')
			time.sleep(1)
			print('\n\n-Repair Droids - yu8xxj3')
			time.sleep(1)
			print('\n\nCODES WILL BE RESET EVERY 24 HOURS')
			security(inventory)
		else:
			print('\n- ACCESS TO DATA RECORDER DENIED -')
			time.sleep(2)
			security(inventory)
		
	elif cmd == '3':
		start(inventory)
		
def observation(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nYou enter the Observation door and are confronted 
with a Enemy Sentry droid beside a disabled crew droid. 
His laser is almost charged and will be active in seconds.\n''')
	print('[-OBSERVATION-]\n')
	print('1.) Terminate Sentry Droid')
	print('2.) Retreat to Main Elevator.')
	
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		if 'laser' in inventory:
			print('\nlaser active...')
			time.sleep(1)
			print('target locked...')
			time.sleep(1)
			print('...')
			time.sleep(1)
			print('\nTARGET TERMINATED\n')
			enemy_sentry(inventory)
		else:
			print('\n- WARNING LASER OFFLINE -')
			time.sleep(2)
			print('''\nThe Sentry Droids laser is now active and has you locked
on. You try to initiate self-destruct but its to late..''')
			print('....')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\nshutdown imminent...')
			time.sleep(1)
			print('CTRL866 offline.')
			time.sleep(1)
			print('Droid terminated.')
			print('\nGAME OVER\n')
			exit(0)
			
	elif cmd == '2':
			print('''\nThe Sentry droids laser is now active and has you locked
on. You try to retreat back to the elevator but its to late..''')
			print('....')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\nshutdown imminent...')
			time.sleep(1)
			print('CTRL866 offline.')
			time.sleep(1)
			print('Droid terminated.')
			print('\nGAME OVER\n')
			exit(0)
			
def enemy_sentry(inventory, items=['motion tracker']):
	print('\n----------')
	time.sleep(1)
	print('''\nThe Enemy Sentry droid has been terminated. 
Judging by the model you know he has a
motion tracker repair program installed. You MUST connect 
to this droid with service port and download the program.''')
	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
	cmdlist = ['service port']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('motion tracker')
			items = ['motion tracker']
			print('\nservice port connected.')
			time.sleep(1)
			print('accessing file..')
			time.sleep(1)
			print('downloading..')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('Repairing Motion Tracker...')
			time.sleep(1)
			print('Auto alignment...')
			time.sleep(1)
			print('....')
			time.sleep(2)
			print('\nMOTION TRACKER ONLINE.')
			time.sleep(2)
			print('''\nYour Motion Tracker is now online.
You return to the main elevator''')
			start(inventory)
			
def shuttle_control(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nYou enter Shuttle Control where all navigation takes place.
A 999 Elite Enemy Command droid is posted here.
This Droid is extremely powerfull.''')
	print('\n[-SHUTTLE CONTROL-]')
	print('\n1.) Terminate the 999 Elite Enemy Command Droid')
	print('2.) Retreat to Main Elevator')
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		if 'laser' in inventory and 'motion tracker' in inventory and 'droid hack' in inventory:
			print('\n....')
			time.sleep(1)
			print('\n....')
			command_droid(inventory)
		else:
			time.sleep(1)
			print('\nEECD999:>')
			print('\n100101010101010101010101010101010' * 10)
			time.sleep(1)
			print('''\nThe Elite Enemy Command droid laughs in machine language
at your pathetic attempt. The last thing your data recorder gets is the
deafing sound of a Target Lock.''')
			print('....')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\nshutdown imminent...')
			time.sleep(1)
			print('CTRL866 offline.')
			time.sleep(1)
			print('Droid terminated.')
			print('\nGAME OVER\n')
			exit(0)
	elif cmd == '2':
		start(inventory)
		
def command_droid(inventory):
	print('\nRunning droid hack...')
	time.sleep(1)
	print('\njamming EECD999 Target Lock...')
	time.sleep(1)
	print('\n......')
	time.sleep(1)
	print('\nMotion Tracker active...')
	time.sleep(1)
	print('\nTrack motion of EECD999...')
	time.sleep(1)
	print('\n......')
	time.sleep(1)
	print('\nLaser active...')
	time.sleep(1)
	print('\nTargeting EECD999...')
	time.sleep(1)
	print('\nTarget Locked...')
	time.sleep(1)
	print('\n......')
	time.sleep(2)
	print('\n\nTARGET TERMINATED \n')
	time.sleep(2)
	print('''\n\nYou have defeated the EECD999 droid and taken back control
of the 'KERNEL'. The flight path has been restored and
a distress signal sent to Droid Command. Reinforcements are inbound.
\n - GAME OVER -\n''')

def getcmd(cmdlist):
	cmd = input('\nCTRL866:> ')
	if cmd in cmdlist:
		return cmd
	elif cmd == 'help':
		print('\nTYPE: inventory to view items')
		print('or quit to self-destruct')
		return getcmd(cmdlist)
	elif cmd == 'inventory':
		print('\ninventory contains:\n')
		for item in inventory:
			print('-- %s' % (item))
		return getcmd(cmdlist)
	elif cmd == 'secret':
		print('\n........')
		time.sleep(1)
		print('\n[--Paradroid -- published by Hewson 1985--]')
		time.sleep(1)
		print('\n[--written by Andrew Braybrook for Commodore 64 computer--]')
		time.sleep(1)
		print('\n[--play this game or die--]')
		time.sleep(1)
		print('\n........\n')
		return getcmd(cmdlist)
	elif cmd == 'quit':
		print('\n----------')
		time.sleep(1)
		print('\nself-destruct sequence initiated...')
		time.sleep(1)
		print('shutdown imminent...')
		time.sleep(1)
		print('\nCTRL866 offline.')
		time.sleep(1)
		print('Droid terminated.\n')
		exit(0)
	else:
		print('\n   error. invalid command-\n')
		return getcmd(cmdlist)
	
if __name__ == "__main__":
	inventory = ['service port']
	start(inventory)