import RPi.GPIO as GPIO
import curses
import time
import random
from curses import wrapper
from websocket import create_connection
ws = create_connection("ws://163.18.2.157:8000/")

GELD_ONE=7
GELD_TWO=11
GELD_THREE=13
GELD_FOUR=15
GELD_FIVE=12
GELD_SIX=16
GELD_SEVEN=18
GELD_EIGHT=22

stdscr = curses.initscr()
stdscr.clear()

try:
 while True:
    web_token = ws.recv()
    if  web_token == "token":
        pi_token = random.choice("@!~&$%^*")
        ws.send(pi_token)
        pi_start = ws.recv()
        game_start = ws.recv()
        if pi_start == pi_token and game_start == 'START' :
            GPIO.cleanup()
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(GELD_ONE,GPIO.OUT)
            GPIO.setup(GELD_TWO,GPIO.OUT)
            GPIO.setup(GELD_THREE,GPIO.OUT)
            GPIO.setup(GELD_FOUR,GPIO.OUT)
            GPIO.setup(GELD_FIVE,GPIO.OUT)
            GPIO.setup(GELD_SIX,GPIO.OUT)
            GPIO.setup(GELD_SEVEN,GPIO.OUT)
            GPIO.setup(GELD_EIGHT,GPIO.OUT)
            print "Setup GPIO"
            while True:
                print "Press button :"
                message = ws.recv()
                #message = stdscr.getkey()
                if message=="GELD_ONE": #1
                    GPIO.output(GELD_ONE,1)
                    time.sleep(3)
                    GPIO.output(GELD_ONE,0)
                    print("ONE")
                    ws.send("ONE")
                if message=="GELD_TWO": #2
                    GPIO.output(GELD_TWO,1)
                    time.sleep(3)
                    GPIO.output(GELD_TWO,0)
                    print("TWO")
                    ws.send("TWO")
                if message=="GELD_THREE": #3
                    GPIO.output(GELD_THREE,1)
                    time.sleep(3)
                    GPIO.output(GELD_THREE,0)
                    print("THREE")
                    ws.send("THREE")
                if message=="GELD_FOUR": #4
                    GPIO.output(GELD_FOUR,1)
                    time.sleep(3)
                    GPIO.output(GELD_FOUR,0)
                    print("FOUR")
                    ws.send("FOUR")
                if message=="GELD_FIVE": #5
                    GPIO.output(GELD_FIVE,1)
                    time.sleep(3)
                    GPIO.output(GELD_FIVE,0)
                    print("FIVE")
                    ws.send("FIVE")
                if message=="GELD_SIX": #6
                    GPIO.output(GELD_SIX,1)
                    time.sleep(3)
                    GPIO.output(GELD_SIX,0)
                    print("SIX")
                    ws.send("SIX")
                if message=="GELD_SEVEN": #7
                    GPIO.output(GELD_SEVEN,1)
                    time.sleep(3)
                    GPIO.output(GELD_SEVEN,0)
                    print("SEVEN")
                    ws.send("SEVEN")
                if message=="GELD_EIGHT": #8
                    GPIO.output(GELD_EIGHT,1)
                    time.sleep(3)
                    GPIO.output(GELD_EIGHT,0)
                    print("EIGHT")
                    ws.send("EIGHT")
                if message=="END":
                    GPIO.output(GELD_ONE,0)
                    GPIO.output(GELD_TWO,0)
                    GPIO.output(GELD_THREE,0)
                    GPIO.output(GELD_FOUR,0)
                    GPIO.output(GELD_FIVE,0)
                    GPIO.output(GELD_SIX,0)
                    GPIO.output(GELD_SEVEN,0)
                    GPIO.output(GELD_EIGHT,0)
                    print("---END---")
                    ws.send("END")
                    break
#                else:
 #                   print("unknow type")
#                   print(message)
 #                   break
  #              break
except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    ws.close()
    GPIO.cleanup()


