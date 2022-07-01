import board
import busio 
import adafruit_pca9685
import time

print("Initializing...")
i2c=busio.I2C(board.SCL,board.SDA)
pca=adafruit_pca9685.PCA9685(i2c)
pca.frequency=60

Lspeed=pca.channels[8]
Lforward=pca.channels[9]
Lbackward=pca.channels[10]

Rbackward=pca.channels[11]
Rforward=pca.channels[12]
Rspeed=pca.channels[13]

def stop():
    Lforward.duty_cycle=0
    Rforward.duty_cycle=0
    Lbackward.duty_cycle=0
    Rbackward.duty_cycle=0

def set_to(left, right):
    MAX = 65535
    lf = True
    rf = True
    if (left < 0):
        left *= -1
        lf = False
    if (right < 0):
        right *= -1
        rf = False
    
    if (lf):
        Lforward.duty_cycle=0xffff
        Lbackward.duty_cycle=0
    else:
        Lforward.duty_cycle=0
        Lbackward.duty_cycle=0xffff

    if (rf):
        Rforward.duty_cycle=0xffff
        Rbackward.duty_cycle=0
    else:
        Rforward.duty_cycle=0
        Rbackward.duty_cycle=0xffff

    Lspeed.duty_cycle=left*MAX//100
    Rspeed.duty_cycle=right*MAX//100


print("Moving forward")
set_to(50,50)
time.sleep(5)
print("Stopping")
set_to(0,0)