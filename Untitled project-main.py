from microbit import *

#opdracht 8
"""while True:
    if button_b.was_pressed():
        pin2.write_digital(1)
        sleep(5000)
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(2000)
        pin1.write_digital(0)
    else:
        pin0.write_digital(1)
        sleep(5000)
        pin0.write_digital(0)"""


"""
#nummer 9
while True:
    if button_b.was_pressed():
        pin2.write_digital(1)
        sleep(5000)
        pin2.write_digital(0)
    if button_a.was_pressed():
        pin0.write_digital(1)
        sleep(5000)
        pin0.write_digital(0)
    else:
        pin1.write_digital(1)
        sleep(2000)
        pin1.write_digital(0)

#oprdracht 10
while True:
    if button_b.was_pressed():
        pin2.write_digital(1)
        sleep(5000)
        pin2.write_digital(0)
    if button_a.was_pressed():
        pin0.write_digital(1)
        sleep(5000)
        pin0.write_digital(0)
    else:
        pin1.write_digital(1)
        sleep(500)
        pin1.write_digital(0)
        sleep(500)"""
"""
#opdracht 11
while True:
    if not button_b.is_pressed():
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)
"""
"""
#opdracht 12
while True:
    if button_a.is_pressed():
        pin2.write_digital(1)
        pin0.write_digital(0)
        pin1.write_digital(0)
    if button_b.is_pressed():
        pin2.write_digital(0)
        pin0.write_digital(1)
        pin1.write_digital(0)
    if button_a.is_pressed() and button_b.is_pressed():
        pin2.write_digital(0)
        pin0.write_digital(0)
        pin1.write_digital(1)
    pin2.write_digital(0)
    pin0.write_digital(0)
    pin1.write_digital(0)
"""

"""
#opdracht 13
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        pin1.write_digital(1)
    pin1.write_digital(0)
"""
"""
#opdracht 14
aantalAutos = 0

while True:
    if button_a.was_pressed() and aantalAutos <9:
        aantalAutos += 1
    if button_b.was_pressed() and aantalAutos != 0:
        aantalAutos -=1
    if aantalAutos ==9:
        pin0.write_digital(1)
        pin2.write_digital(0)
    else:
        pin2.write_digital(1)
        pin0.write_digital(0)
    display.show(aantalAutos)
"""

"""
#opracht 15
while True:
    print(pin8.read_digital())
    if pin8.read_digital():
        pin1.write_digital(0)
        pin2.write_digital(1)
    elif not pin8.read_digital():
        pin2.write_digital(0)
        pin1.write_digital(1)
"""
"""
#opdracht 16
getal =1
while True:
    if button_a.was_pressed():
        getal = getal *2
    if button_b.was_pressed() and getal !=1:
        getal = getal/2
    display.show(int(getal))
"""
"""
#opdracht17 
aantalAutos = 0

while True:
    if button_a.was_pressed() and aantalAutos <9:
        aantalAutos += 1
    if button_b.was_pressed() and aantalAutos != 0:
        aantalAutos -=1
    if aantalAutos ==9:
        pin0.write_digital(1)
        pin2.write_digital(0)
    else:
        pin2.write_digital(1)
        pin0.write_digital(0)
    display.show(9 - aantalAutos)
"""
"""
#opdracht18
aantalAutos = 0

while True:
    if button_a.was_pressed() and aantalAutos <9:
        print("er is een auto de garag binnen gereden")
        aantalAutos += 1
    if button_b.was_pressed() and aantalAutos != 0:
        print("er is een auto de garag buiten gereden")
        aantalAutos -=1
    if aantalAutos ==9:
        pin0.write_digital(1)
        pin2.write_digital(0)
    else:
        pin2.write_digital(1)
        pin0.write_digital(0)
    display.show(9 - aantalAutos)
"""
"""
#opdracht 19
while True:
    if display.read_light_level() <= 60:
        pin2.write_digital(1)
        pin1.write_digital(1)
        pin0.write_digital(1)
    elif display.read_light_level() <= 120:
        pin2.write_digital(1)
        pin1.write_digital(1)
        pin0.write_digital(0)
    elif display.read_light_level() <= 240:
        pin2.write_digital(1)
        pin1.write_digital(0)
        pin0.write_digital(0)
"""
"""
#opdracht 20
while True:
    if button_a.was_pressed():
        for i in range(10):
            display.show(i)
"""
"""
#opdracht 21
getal = 0
while True:
    if button_a.is_pressed():
        getal+=1
        display.show(getal)
        sleep(1000)
    else:
        getal=0
        display.show(getal)
"""
"""
#opdracht 22
import random
getal = 0
while True:
    if button_a.is_pressed():
        getal = random.randint(1,6)
    else:
        display.show(getal)
"""
"""
#opdracht 23
punten_iot = [13,15,3,9,11,10,18,17,5,12,11,5]

while True:
    for i in punten_iot:
        print(i)
"""
"""
#opdracht 24
kleuren = ["groen" , "oranje" , "rood"] 

while True:
    for i in kleuren:
        print(i)
"""
"""
#opdracht 25
punten_iot = [13,15,3,9,11,10,18,17,5,12,11,5]

print(punten_iot[0])
print(punten_iot[11])
"""
"""
#opdracht 26
kleuren = ["groen" , "oranje" , "rood"] 

print(kleuren[1])
kleuren[1] = "Geel"
print(kleuren[1])
"""
"""
#opdracht 27
def RoodLicht():
    print("rood")
    delay = 5000
    pin0.write_digital(1)
    sleep(delay)
    pin0.write_digital(0)
def oranjeLicht():
    print("oranje")
    delay = 2000
    pin1.write_digital(1)
    sleep(delay)
    pin1.write_digital(0)
def groenLicht():
    print("groen")
    delay = 5000
    pin2.write_digital(1)
    sleep(delay)
    pin2.write_digital(0)

while True:
    RoodLicht()
    oranjeLicht()
    groenLicht()
"""
"""
#opdracht 28
def RoodLicht(delay):
    print("rood")
    pin0.write_digital(1)
    sleep(delay)
    pin0.write_digital(0)
def oranjeLicht(delay):
    print("oranje")
    pin1.write_digital(1)
    sleep(delay)
    pin1.write_digital(0)
def groenLicht(delay):
    print("groen")
    pin2.write_digital(1)
    sleep(delay)
    pin2.write_digital(0)

while True:
    RoodLicht(250)
    oranjeLicht(500)
    groenLicht(1000)
"""
"""
#opdracht 29
def RoodLicht(delay , aantal_knipperen):
    print("rood")
    for i in range(aantal_knipperen):
        pin0.write_digital(1)
        sleep(delay)
        pin0.write_digital(0)
        sleep(delay)
    return delay*aantal_knipperen
    
def oranjeLicht(delay, aantal_knipperen):
    print("oranje")
    for i in range(aantal_knipperen):
        pin1.write_digital(1)
        sleep(delay)
        pin1.write_digital(0)
        sleep(delay)
    return delay*aantal_knipperen
    
def groenLicht(delay, aantal_knipperen):
    print("groen")
    for i in range(aantal_knipperen):
        pin2.write_digital(1)
        sleep(delay)
        pin2.write_digital(0)
        sleep(delay)
    return delay*aantal_knipperen
    
while True:
    if button_a.was_pressed():
        RoodLicht(250 ,5)
    if button_b.was_pressed():
        oranjeLicht(500,4)
    if button_a.is_pressed() and button_b.is_pressed():
        groenLicht(1000,2)
"""
"""
#extra oef 1
xvalue =0 
yvalue =0
while True:
    if button_a.was_pressed():
            for x in range(5):
                display.set_pixel(x,yvalue,9)
                sleep(500)
    if button_b.was_pressed():
        display.clear()
"""
"""
#extra oef 2
xvalue =4
yvalue =0
while True:
    if button_a.was_pressed():
            for x in range(5):
                display.set_pixel(x,yvalue,9)
                sleep(500)
                display.set_pixel(x,yvalue,0)
    if button_b.was_pressed():
        for x in range(5):
                display.set_pixel((xvalue-x),yvalue,9)
                sleep(500)
                display.set_pixel((xvalue-x),yvalue,0)
"""
"""
#extra oef 3
xvalue =0
yvalue =4
while True:
    if button_a.was_pressed():
            for y in range(5):
                display.set_pixel(xvalue,y,9)
                sleep(500)
                display.set_pixel(xvalue,y,0)
    if button_b.was_pressed():
        for y in range(5):
                display.set_pixel(xvalue,(yvalue-y),9)
                sleep(500)
                display.set_pixel(xvalue,(yvalue-y),0)
"""
"""
#extra oef 4
xvalue =4
yvalue =4
while True:
    if button_a.was_pressed():
            for locatie in range(5):
                display.set_pixel((xvalue-locatie),locatie,9)
                sleep(500)
                display.set_pixel((xvalue-locatie),locatie,0)
"""
"""
#extra oef 5
xvalue =0 
yvalue =0
while True:
    if button_a.was_pressed():
        for y in range(5):
            for x in range(5):
                display.set_pixel(x,y,9)
                sleep(500)
    if button_b.was_pressed():
        display.clear()
"""
"""
#extra oef 6
xvalue =4
yvalue =4
while True:
    if button_a.was_pressed():
        for y in range(5):
            for x in range(5):
                display.set_pixel(x,y,9)
                sleep(500)
                display.set_pixel(x,y,0)
    if button_b.was_pressed():
        for y in range(5):
            for x in range(5):
                display.set_pixel((xvalue-x),(yvalue-y),9)
                sleep(500)
                display.set_pixel((xvalue-x),(yvalue-y),0)
"""
"""
#extra oef 7
xvalue =4 
yvalue =4
while True:
    if button_a.was_pressed():
        for y in range(5):
            for x in range(5):
                if(y%2==0):
                    display.set_pixel(x,y,9)
                    sleep(500)
                else:
                    display.set_pixel((xvalue-x),y,9)
                    sleep(500)
    if button_b.was_pressed():
        display.clear()
"""
"""
#extra oef 8
xvalue =4 
yvalue =4
while True:
    if button_a.was_pressed():
        for y in range(5):
            for x in range(5):
                if(y%2==0):
                    display.set_pixel(x,y,9)
                    sleep(500)
                    display.set_pixel(x,y,0)
                else:
                    display.set_pixel((xvalue-x),y,9)
                    sleep(500)
                    display.set_pixel((xvalue-x),y,0)
    if button_b.was_pressed():
        for y in range(5):
            for x in range(5):
                if(y%2==0):
                    display.set_pixel(x,(yvalue-y),9)
                    sleep(500)
                    display.set_pixel(x,(yvalue-y),0)
                else:
                    display.set_pixel((xvalue-x),(yvalue-y),9)
                    sleep(500)
                    display.set_pixel((xvalue-x),(yvalue-y),0)
"""
"""
#extra oef 9
xvalue =4 
yvalue =4
while True:
    if button_a.was_pressed():
            for x in range(5):
                    display.set_pixel(x,0,9)
                    sleep(500)
                    display.set_pixel(x,0,0)
            for y in range(5):
                display.set_pixel(4,y,9)
                sleep(500)
                display.set_pixel(4,y,0)
            for x in range(5):
                    display.set_pixel((xvalue-x),4,9)
                    sleep(500)
                    display.set_pixel((xvalue-x),4,0)
            for y in range(5):
                display.set_pixel(0,(yvalue-y),9)
                sleep(500)
                display.set_pixel(0,(yvalue-y),0)
    if button_b.was_pressed():
        for y in range(5):
                display.set_pixel(0,y,9)
                sleep(500)
                display.set_pixel(0,y,0)
        for x in range(5):
                display.set_pixel(x,4,9)
                sleep(500)
                display.set_pixel(x,4,0)
        for y in range(5):
                display.set_pixel(4,(yvalue-y),9)
                sleep(500)
                display.set_pixel(4,(yvalue-y),0)
        for x in range(5):
                    display.set_pixel((xvalue-x),0,9)
                    sleep(500)
                    display.set_pixel((xvalue-x),0,0)
"""

#extre oef 10
xvalue =4 
yvalue =4
aantalherhalingen = [5,3]
getal = -1
while True:
    if button_a.was_pressed():
        for aantal in aantalherhalingen:
            getal+=1
            for x in range(aantal):
                        display.set_pixel(x+getal,0+getal,9)
                        sleep(500)
            for y in range(aantal):
                    display.set_pixel(4-getal,y+getal,9)
                    sleep(500)
            for x in range(aantal):
                        display.set_pixel((xvalue-x)-getal,4-getal,9)
                        sleep(500)
            for y in range(aantal):
                    display.set_pixel(0+getal,(yvalue-y)-getal,9)
                    sleep(500)
        display.set_pixel(2,2,9)
        
        





















