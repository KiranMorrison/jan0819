import winsound
import time
bpm = input('please insert bpm')
s = 60/int(bpm)
print('A half beat is {}s'.format(s))
b = int(1000*s)
print('A rest will be {}ms'.format(b))
time.sleep(s)
winsound.Beep(349, b) # F
time.sleep(s)
winsound.Beep(440, b) # A
winsound.Beep(523, b) # C
time.sleep(s)
winsound.Beep(440, b) # A
time.sleep(s)
winsound.Beep(349, b) # F
winsound.Beep(293, b) # D
winsound.Beep(293, b) # D
winsound.Beep(293, b) # D
time.sleep(4*s)
winsound.Beep(261, b) # C
winsound.Beep(293, b) # D
winsound.Beep(349, b) # F
winsound.Beep(440, b) # A
winsound.Beep(523, 3*b) # C
time.sleep(0.5*s)
winsound.Beep(440, b) # A
time.sleep(0.5*s)
winsound.Beep(349, b) # F
winsound.Beep(660, 3*b) # E
winsound.Beep(622, b) # Eb
winsound.Beep(587, b) # D
time.sleep(3*s)