# Working with servos
import board, time, pwmio, digitalio

from adafruit_motor import servo
from analogio import AnalogIn
from adafruit_debouncer import Debouncer

button_A= digitalio.DigitalInOut(board.D6)
button_A.switch_to_input(pull=digitalio.Pull.UP)
switch= Debouncer(button_A)

pwm = pwmio.PWMOut(board.D4, frequency=50)
pwm2 = pwmio.PWMOut(board.D5, frequency=50)
servo_1 = servo.Servo(pwm, max_pulse = 2500)
servo_2= servo.Servo(pwm2, max_pulse = 2500)
check=1

servo_1.angle= 180
servo_2.angle= 180

while True:
    switch.update()
    if switch.fell:
        if check==1:
            servo_1.angle= 90
            servo_2.angle= 90
            print(check)
            check-=1
        else:
            servo_1.angle =180
            servo_2.angle =180
            print(check)
            check+=1

