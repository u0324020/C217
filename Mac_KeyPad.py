import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)

MATRIX = [ [7,3,'#'],
           [5,1,9],
           [6,2,'*'],
           [4,0,8]]

ROW = [12,16,7,11]#7.11.12.16
COL = [22,15,13]#13.15.22

counts = 0
GN_1 = ''
GN_2 = ''
GN_3 = ''

for j in range(3):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range (4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while(True):
        for j in range (3):
            GPIO.output(COL[j],0)

            for i in range(4):
               if GPIO.input (ROW[i]) == 0 :
                    if counts < 3 :
                        if MATRIX[i][j] == '#':
                            counts = counts - 1
                            pass
                        if counts == 0 :
                            GN_1 = MATRIX[i][j]
                            if GN_1 == '#':
                                GN_1 = ''
                                print('Cancel....')
                                break
                            if GN_1 != '#' or '*':
                                print ('You Enter:%s')%(MATRIX[i][j])
                                time.sleep(1)
                                counts = counts + 1
                                break
                            break
                        if counts == 1 and GN_1 != '' and MATRIX[i][j] != '*':
                            GN_2 = MATRIX[i][j]
                            if GN_2 == '#':
                                GN_2 = ''
                                counts = 1
                                continue
                            if GN_2 != '#' or '*' and GN_1 != '#':
                                print('You Enter:%s%s')%(GN_1,GN_2)
                                print('Please enter confirm...')
                                time.sleep(1)
                                counts = counts + 1
                                break
                            break
                        if counts != 0 and MATRIX[i][j] == '*':
                            print('------Confirm Your Enter is :%s%s -------' )%(GN_1,GN_2)
                            counts = 0
                            pass

                    time.sleep(1)
                    while (GPIO.input(ROW[i]) == 0):
                        pass
                    counts = counts + 1

            GPIO.output(COL[j],1)
except KeyboardInterrupt:
    GPIO.cleanup()