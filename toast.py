import board, neopixel, time, adafruit_vl53l1x, math
import digitalio
import touchio
from adafruit_debouncer import Debouncer
from digitalio import DigitalInOut, Direction, Pull

i2c= board.I2C()
distance_sensor = adafruit_vl53l1x.VL53L1X(i2c)
distance_sensor.distance_mode=1
distance_sensor.timing_budget=100
distance_sensor.start_ranging()

reset=0


strip_pin=board.A1
strip_num_of_lights=30
strip=neopixel.NeoPixel(strip_pin, strip_num_of_lights, brightness=0.5, auto_write=True)
touchpas_TX=touchio.TouchIn(board.TX)


strip.fill((0,0,0))
switch = DigitalInOut(board.A3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
button= Debouncer(switch)

RED= (255,0,0)
ORANGE=(255, 36, 0)

def light_timing(distance):
    time=0
    max_dist= 30
    min_dist = 2
    if (distance<8 and distance >1):
        time = 0.2
    elif(distance<14 and distance >7):
        time = 0.4
    elif(distance<20 and distance >13):
        time=0.6
    elif(distance<30 and distance>19):
        time=0.8
    return time





def fire(count):
    while True:
        button.update()
        if button.fell:
            break
        else:
            if count==0:
                for i in range(30):
                    if i<5:
                        strip[i]=ORANGE
                    elif i>4 and i<10:
                        strip[i]=RED
                    elif i>9 and i<15:
                        strip[i]=ORANGE
                    elif i>14 and i<20:
                        strip[i]=RED
                    elif i>19 and i<25:
                        strip[i]=ORANGE
                    elif i>24 and i<30:
                        strip[i]=RED
                count+=1
            else:
                for i in range(30):
                    if i<5:
                        strip[i]=RED
                    elif i>4 and i<10:
                        strip[i]=ORANGE
                    elif i>9 and i<15:
                        strip[i]=RED
                    elif i>14 and i<20:
                        strip[i]=ORANGE
                    elif i>19 and i<25:
                        strip[i]=RED
                    elif i>24 and i<30:
                        strip[i]=ORANGE
                count-=1
    print("0")


while True:
    button.update()
    if button.fell:
        reset = 1
        strip.fill((255,255,255))
        count=0
        count1=255
        count2=255
        count3=255
    if(reset==1):
        if touchpas_TX.value:
            if distance_sensor.data_ready:
                distance = distance_sensor.distance
                print(f"Distance: {distance}")
                strip.fill((count1,count2,count3))
                count2-=3
                if(count3>5):
                    count3-=7
                if(count2<5):
                    if(fire(count) ==0):
                        reset=0
                if(distance>1 and distance<30):
                    timing= light_timing(distance)
                time.sleep(timing)




