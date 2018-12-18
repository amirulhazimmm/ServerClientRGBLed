import socket, sys, time, datetime
from _thread import *
import RPi.GPIO as GPIO
import time
    
## Define Pin on Raspberry Pi
rPin = 27
bPin = 17
gPin = 22

## Function to turn on pin
def turnOn(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

## Function to turn off pin
def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW) 

def redOn():
    turnOn(rPin)
    
def greenOn():
    turnOn(gPin)

def blueOn():
    turnOn(bPin)

def redOff():
    turnOff(rPin)

def greenOff():
    turnOff(gPin)
    
def blueOff():
    turnOff(bPin)

########################################################
    
## Host '' means that we enable any host to enter
host = ''
port = 25000

## Create Socket Function
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[SERVER]Socket Created")

## To bind Function
try:
    s.bind((host,port))
except socket.error:
    print("[SERVER]Binding Failed")
    sys.exit()

print("[SERVER]Socket has been binded")

## To listen function, 10 mean up to 10 people able to queue to handle a request
s.listen(10)

print("[SERVER]Socket Is Ready\n")

## Function for multi client
def clientthread(conn):
    
    ## Function to send    
    welcomemsg = "Raspberry Pi RGB LED Controller"
    conn.send(welcomemsg.encode())

    while True:
        ##Function to receive
        data = conn.recv(4096)
        if not data:
            break;
        reply = "<Client> " + data.decode()
        print(reply)
        uInput = data.decode()

        if uInput == "red on":
            redOn()
        elif uInput == "red off":
            redOff()
        elif uInput == "green on":
            greenOn()
        elif uInput == "green off":
            greenOff()
        elif uInput == "blue on":
            blueOn()
        elif uInput == "blue off":
            blueOff()
        else:
            print("Invalid command")
            
    conn.close()

## Function to save connection into file
def saveFile(addr):
    f = open("conLog.txt", "a+")

    msg = "hello\n"

    f.write(msg)
   
while 1:
    ## To accept function
    conn, addr = s.accept()
    saveFile(addr)
    print("[SERVER]Connected with " + addr[0] + ":" + str(addr[1]) + "\n")
    start_new_thread(clientthread, (conn,))
    
s.close()
