#Juan David Casallas
'''
#EJERCICIO 1 BASE 
from time import sleep 
from machine import Pin as pin 
from utime import sleep as pausa, sleep_ms as pausam 
pausa=0.2 
leda=pin(22,pin.OUT) 
ledb=pin(19,pin.OUT) 
ledc=pin(23,pin.OUT) 
ledd=pin(1,pin.OUT) 
lede=pin(21,pin.OUT) 
ledf=pin(18,pin.OUT) 
ledg=pin(17,pin.OUT) 
ledh=pin(4,pin.OUT) 
ledi=pin(2,pin.OUT) 
ledj=pin(15,pin.OUT) 
 
while True: 
    leda.value(1) 
    sleep(pausa) 
    leda.value(0) 
    sleep(pausa) 
    ledb.value(1) 
    sleep(pausa) 
    ledb.value(0) 
    sleep(pausa) 
    ledc.value(1) 
    sleep(pausa) 
    ledc.value(0) 
    sleep(pausa) 
    ledd.value(1) 
    sleep(pausa) 
    ledd.value(0) 
    sleep(pausa) 
    lede.value(1) 
    sleep(pausa) 
    lede.value(0) 
    sleep(pausa) 
    ledf.value(1) 
    sleep(pausa) 
    ledf.value(0) 
    sleep(pausa) 
    ledg.value(1) 
    sleep(pausa) 
    ledg.value(0) 
    sleep(pausa) 
    ledh.value(1) 
    sleep(pausa) 
    ledh.value(0) 
    sleep(pausa) 
    ledi.value(1) 
    sleep(pausa) 
    ledi.value(0) 
    sleep(pausa) 
    ledj.value(1) 
    sleep(pausa) 
    ledj.value(0) 
    sleep(pausa) 
'''
'''
#EJERCICIO2 FUNCIONES
from machine import Pin as pin 
from utime import sleep as pausa, sleep_ms as pausam 
leda=pin(22,pin.OUT) 
ledb=pin(19,pin.OUT) 
ledc=pin(23,pin.OUT) 
ledd=pin(1,pin.OUT) 
lede=pin(21,pin.OUT) 
ledf=pin(18,pin.OUT) 
ledg=pin(17,pin.OUT) 
ledh=pin(4,pin.OUT) 
ledi=pin(2,pin.OUT) 
ledj=pin(15,pin.OUT) 
 
def print_led(a,b,c,d,e,f,g,h,i,j): 
    leda.value(a),ledb.value(b),ledc.value(c),ledd.value(d),lede.value(e),ledf.value(f),ledg.value(g),ledh.value(h),ledi.value(i),ledj.value(j) 
    pausam(200) 
while True: 
    print_led(0,0,0,0,0,0,0,0,0,1) 
    print_led(0,0,0,0,0,0,0,0,1,0) 
    print_led(0,0,0,0,0,0,0,1,0,0) 
    print_led(0,0,0,0,0,0,1,0,0,0) 
    print_led(0,0,0,0,0,1,0,0,0,0) 
    print_led(0,0,0,0,1,0,0,0,0,0) 
    print_led(0,0,0,1,0,0,0,0,0,0) 
    print_led(0,0,1,0,0,0,0,0,0,0) 
    print_led(0,1,0,0,0,0,0,0,0,0) 
    print_led(1,0,0,0,0,0,0,0,0,0) 
'''
'''
#EJERCICIO 3 LISTAS
from machine import Pin as pin 
from utime import sleep as pausa, sleep_ms as pausam 
leda=pin(22,pin.OUT) 
ledb=pin(19,pin.OUT) 
ledc=pin(23,pin.OUT) 
ledd=pin(1,pin.OUT) 
lede=pin(21,pin.OUT) 
ledf=pin(18,pin.OUT) 
ledg=pin(17,pin.OUT) 
ledh=pin(4,pin.OUT) 
ledi=pin(2,pin.OUT) 
ledj=pin(15,pin.OUT)

lista1=[leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi,ledj]

while True:
    
    for led in lista1:
        led.value(1)
        pausa(0.3)
        led.value(0)
        pausa(0.03)
    print(led)
    
'''
'''
#EJERCICIO 4 LISTAS Y DOBLE FOR UTILIZANDO NOT
from machine import Pin as pin 
from utime import sleep as pausa, sleep_ms as pausam 
leda=pin(22,pin.OUT) 
ledb=pin(19,pin.OUT) 
ledc=pin(23,pin.OUT) 
ledd=pin(1,pin.OUT) 
lede=pin(21,pin.OUT) 
ledf=pin(18,pin.OUT) 
ledg=pin(17,pin.OUT) 
ledh=pin(4,pin.OUT) 
ledi=pin(2,pin.OUT) 
ledj=pin(15,pin.OUT)

lista1=[leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi,ledj]

while True:
    
    for led in lista1:
        for led2 in range(2):
            led.value(not led.value())
            pausam(100)
    print(led)
'''

#EJERCICIO 5 LISTAS PARA INSTANCIAMIENTO
from machine import Pin as pin 
from utime import sleep as pausa, sleep_ms as pausam

entradaspin=[22,19,23,1,21,18,17,4,2,15]
asignacionpin=[]

for i in entradaspin:
    asignacionpin.append(pin(i,pin.OUT))

while True:
    
    for led in asignacionpin:
        for led2 in range(2):
            led.value(not led.value())
            pausam(50)
    print(led)


#Juan David Casallas 