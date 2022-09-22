import math
from machine import Pin as pin, ADC, I2C
from utime import sleep_ms
from sdd1306 import SSD1306_I2C
import framebuf
sensorx = ADC(pin(32))            # pines usados el 35,34,33,36, 39 , 32,
sensory = ADC(pin(33))            # pines usados el 35,34,33,36, 39 , 32,
boton = pin(4, pin.IN,pin.PULL_UP)#pin boton jostick
confirmador = pin(21, pin.IN)     #pin modulo

sensorx.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensorx.width(ADC.WIDTH_12BIT)  # establecer resolución
sensory.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensory.width(ADC.WIDTH_12BIT)  # establecer resolución
ancho = 128
alto = 64
i2c = I2C(0, scl=pin(22), sda=pin(23))
oled = SSD1306_I2C(ancho, alto, i2c)
# print(i2c.scan())
def imprime(valx,valy):#FUNCION EQUIS
    ciry=(10+(valy*18)+9)
    cirx=(0+(valx*42)+21)
    oled.line(cirx,ciry,cirx+20,ciry+9,0)
    oled.line(cirx,ciry,cirx+20,ciry-9,0)
    oled.line(cirx,ciry,cirx-20,ciry+9,0)
    oled.line(cirx,ciry,cirx-20,ciry-9,0)
    
def carita(a,b,c,d,f,g): #FUNCION CIRCULO
    for anguloGrados in range(a, b, c):                    # Ángulo de giro de la línea del eje (de 0º a 360º en intervalos de 5º)
        anguloRadianes = (math.pi*anguloGrados)/180          # Ángulo de giro de la línea del eje en radianes
        xLinea = int(math.cos(anguloRadianes)*d)            # Coordenada x línea del eje 
        yLinea = int(math.sin(anguloRadianes)*d)
        #print (f"x:{xLinea}y:{yLinea}")    
        #print (yLinea)    
        oled.pixel (xLinea+f,yLinea+g,0)
    #oled.show()

def circulo(valx,valy):#FUNCION CIRCULO
    ciry=(10+(valy*18)+9)
    cirx=(0+(valx*42)+21)
    carita(0,360,1,10,cirx,ciry,)
cont=0   
cox=1#CIRCULO O EQUIS 

bandera_1 = [False, 'n']
bandera_2 = [False, 'n']
bandera_3 = [False, 'n']
bandera_4 = [False, 'n']
bandera_5 = [False, 'n']
bandera_6 = [False, 'n']
bandera_7 = [False, 'n']
bandera_8 = [False, 'n']
bandera_9 = [False, 'n']   

estado_triqui=[[0,0,0],
               [0,0,0],
               [0,0,0]]

def valida_ganador(estado_triqui):
    if estado_triqui[0][0] == estado_triqui[1][0] and estado_triqui[1][0] == estado_triqui[2][0] and estado_triqui[0][0] != 0:
        return estado_triqui[0][0]
    elif estado_triqui[0][1] == estado_triqui[1][1] and estado_triqui[1][1] == estado_triqui[2][1] and estado_triqui[0][1] != 0:
        return estado_triqui[0][1]
    elif estado_triqui[0][2] == estado_triqui[1][2] and estado_triqui[1][2] == estado_triqui[2][2] and estado_triqui[0][2] != 0:
        return estado_triqui[0][2]
        
    elif estado_triqui[0][0] == estado_triqui[0][1] and estado_triqui[0][1] == estado_triqui[0][2] and estado_triqui[0][0] != 0:
        return estado_triqui[0][0]
    elif estado_triqui[1][0] == estado_triqui[1][1] and estado_triqui[1][1] == estado_triqui[1][2] and estado_triqui[1][0] != 0:
        return estado_triqui[1][0]
    elif estado_triqui[2][0] == estado_triqui[2][1] and estado_triqui[2][1] == estado_triqui[2][2] and estado_triqui[2][0] != 0:
        return estado_triqui[2][0]
        
    elif estado_triqui[0][0] == estado_triqui[1][1] and estado_triqui[1][1] == estado_triqui[2][2] and estado_triqui[0][0] != 0:
        return estado_triqui[0][0]
    elif estado_triqui[0][2] == estado_triqui[1][1] and estado_triqui[1][1] == estado_triqui[2][0] and estado_triqui[0][2] != 0:
        return estado_triqui[0][2]
    elif estado_triqui[0][0] != 0 and estado_triqui[0][1] != 0 and estado_triqui[0][2] != 0 and estado_triqui[1][0] != 0 and estado_triqui[1][1] != 0 and estado_triqui[1][2] != 0 and estado_triqui[2][0] != 0 and estado_triqui[2][1] != 0 and estado_triqui[2][2] != 0:
        return 'EMPATE'
    else:
        return 0
    
    
cadena = ""
val_fin = False

while True:
    oled.fill(1)
    oled.text("Buen Dia!", 30, 2, 0)
    oled.text("Game Avaible:", 15, 10, 0)
    oled.text("TRIQUI", 40, 20, 0)
    oled.line(40, 28, 88, 28, 0)
    oled.text("Oprime el boton", 5, 36, 0)
    oled.text("amarillo", 30, 44, 0)
    oled.text("para iniciar", 17, 52, 0) 
    if confirmador.value():
        sleep_ms(500)
        confirmador.value(1)
        
        bandera_1 = [False, 'n']
        bandera_2 = [False, 'n']
        bandera_3 = [False, 'n']
        bandera_4 = [False, 'n']
        bandera_5 = [False, 'n']
        bandera_6 = [False, 'n']
        bandera_7 = [False, 'n']
        bandera_8 = [False, 'n']
        bandera_9 = [False, 'n']   

        estado_triqui=[[0,0,0],
                    [0,0,0],
                    [0,0,0]]
        cont=0
        cadena = ""
        val_fin = False
        
        while True:
            x = sensorx.read()
            y = sensory.read()
            oled.fill(1)
            oled.text("TRIQUI-UMB", 23, 2, 0)
            oled.line(42, 12, 42, 60, 0)  # LINEA VERTICAL DERECHA
            oled.line(84, 12, 84, 60, 0)  # LINEA VERTICAL IZQUIERDA
            oled.line(5, 28, 120, 28, 0)  # LINEA HORIZONTAL ARRIBA
            oled.line(5, 46, 120, 46, 0)  # LINEA HORIZONTAL ABAJO
            oled.text(f"T{cox}", 110, 2, 0)

            if bandera_1[0] == True:
                if bandera_1[1] == 'x':
                    imprime(0,0)
                else:
                    circulo(0,0)
            if  bandera_2[0] == True:
                if bandera_2[1] == 'x':
                    imprime(0,1)
                else:
                    circulo(0,1)
            if  bandera_3[0] == True:
                if bandera_3[1] == 'x':
                    imprime(0,2)
                else:
                    circulo(0,2)
                    
            if bandera_4[0] == True:
                if bandera_4[1] == 'x':
                    imprime(1,0)
                else:
                    circulo(1,0)
            if  bandera_5[0] == True:
                if bandera_5[1] == 'x':
                    imprime(1,1)
                else:
                    circulo(1,1)
            if  bandera_6[0] == True:
                if bandera_6[1] == 'x':
                    imprime(1,2)
                else:
                    circulo(1,2)
                    
            if bandera_7[0] == True:
                if bandera_7[1] == 'x':
                    imprime(2,0)
                else:
                    circulo(2,0)
            if  bandera_8[0] == True:
                if bandera_8[1] == 'x':
                    imprime(2,1)
                else:
                    circulo(2,1)
            if  bandera_9[0] == True:
                if bandera_9[1] == 'x':
                    imprime(2,2)
                else:
                    circulo(2,2)
        #EQUIS X
            if val_fin == False:
                if cox %2 == 0:
                    if x > 3600 and y > 3600:                      # ARRIBA E IZQUIERDA
                        if estado_triqui[0][0]==0:
                            imprime(0,0)
                            print(f"Turno # {cox} Turno de EQUIS X")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_1[0] = True
                                bandera_1[1] = 'x'
                                estado_triqui[0][0] = 'X'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif x > 3600 and not y > 3600 and not y < 150:  #IZQUIERDA
                        if estado_triqui[0][1]==0:
                            imprime(0,1)
                            print(f"Turno # {cox} Turno de EQUIS X")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_2[0] = True
                                bandera_2[1] = 'x'
                                estado_triqui[0][1] = 'X'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif y < 150 and x > 3600:                       # ABAJO E IZQUIERDA
                        if estado_triqui[0][2]==0:
                            imprime(0,2)
                            print(f"Turno # {cox} Turno de EQUIS X")
                            print('Abajo e Izquierda')
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_3[0] = True
                                bandera_3[1] = 'x'
                                estado_triqui[0][2] = 'X'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")   
                            
                                        
                    elif y > 3600 and not x > 3600 and not x < 150:  # ARRIBA
                        if estado_triqui[1][0]==0:
                            imprime(1,0)
                            print(f"Turno # {cox} Turno de EQUIS X")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_4[0] = True
                                bandera_4[1] = 'x'
                                estado_triqui[1][0] = 'X'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif boton.value()==0:                           #CENTRO
                        if estado_triqui[1][1]==0:
                            imprime(1,1)
                            print(f"Turno # {cox} Turno de EQUIS X")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_5[0] = True
                                bandera_5[1] = 'x'
                                estado_triqui[1][1] = 'X'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado") 
                    elif y < 150 and not x > 3600 and not x < 150:   # ABAJO
                        if estado_triqui[1][2]==0:
                            imprime(1,2)
                            print(f"Turno # {cox} Turno de EQUIS X")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_6[0] = True
                                bandera_6[1] = 'x'
                                estado_triqui[1][2] = 'X'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado") 
                    elif x < 150 and y > 3600:                       # ARRIBA Y DERECHA
                        if estado_triqui[2][0]==0:
                            imprime(2,0)
                            print(f"Turno # {cox} Turno de EQUIS X")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_7[0] = True
                                bandera_7[1] = 'x'
                                estado_triqui[2][0] = 'X'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado") 
                    elif x < 150 and not y > 3600 and not y < 150:  # DERECHA
                        if estado_triqui[2][1]==0:
                            imprime(2,1)
                            print(f"Turno # {cox} Turno de EQUIS X")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_8[0] = True
                                bandera_8[1] = 'x'
                                estado_triqui[2][1] = 'X'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif y < 150 and x < 150:                       # ABAJO Y DERECHA
                        if estado_triqui[2][2]==0:
                            imprime(2,2)
                            print(f"Turno # {cox} Turno de EQUIS X")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_9[0] = True
                                bandera_9[1] = 'x'
                                estado_triqui[2][2] = 'X'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif confirmador.value():
                        confirmador.value(1)
                        cox+=1
                        print(f"Cambio de turno {cox}")
            #CIRCULO            
                else:
                    if x > 3600 and y > 3600:                      # ARRIBA E IZQUIERDA
                        if estado_triqui[0][0]==0:
                            circulo(0,0)
                            print(f"Turno # {cox} Turno de CIRCULO O")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_1[0] = True
                                bandera_1[1] = 'o'
                                estado_triqui[0][0] = 'O'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif x > 3600 and not y > 3600 and not y < 150:  #IZQUIERDA
                        if estado_triqui[0][1]==0:
                            circulo(0,1)
                            print(f"Turno # {cox} Turno de CIRCULO O")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_2[0] = True
                                bandera_2[1] = 'o'
                                estado_triqui[0][1] = 'O'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif y < 150 and x > 3600:                       # ABAJO E IZQUIERDA
                        if estado_triqui[0][2]==0:
                            circulo(0,2)
                            print(f"Turno # {cox} Turno de CIRCULO O")
                            print('Abajo e Izquierda')
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_3[0] = True
                                bandera_3[1] = 'o'
                                estado_triqui[0][2] = 'O'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")   
                            
                                        
                    elif y > 3600 and not x > 3600 and not x < 150:  # ARRIBA
                        if estado_triqui[1][0]==0:
                            circulo(1,0)
                            print(f"Turno # {cox} Turno de CIRCULO O")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_4[0] = True
                                bandera_4[1] = 'o'
                                estado_triqui[1][0] = 'O'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif boton.value()==0:                           #CENTRO
                        if estado_triqui[1][1]==0:
                            circulo(1,1)
                            print(f"Turno # {cox} Turno de CIRCULO O")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_5[0] = True
                                bandera_5[1] = 'o'
                                estado_triqui[1][1] = 'O'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado") 
                    elif y < 150 and not x > 3600 and not x < 150:   # ABAJO
                        if estado_triqui[1][2]==0:
                            circulo(1,2)
                            print(f"Turno # {cox} Turno de CIRCULO O")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_6[0] = True
                                bandera_6[1] = 'o'
                                estado_triqui[1][2] = 'O'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado") 
                    elif x < 150 and y > 3600:                       # ARRIBA Y DERECHA
                        if estado_triqui[2][0]==0:
                            circulo(2,0)
                            print(f"Turno # {cox} Turno de CIRCULO O")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_7[0] = True
                                bandera_7[1] = 'o'
                                estado_triqui[2][0] = 'O'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado") 
                    elif x < 150 and not y > 3600 and not y < 150:  # DERECHA
                        if estado_triqui[2][1]==0:
                            circulo(2,1)
                            print(f"Turno # {cox} Turno de CIRCULO O")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_8[0] = True
                                bandera_8[1] = 'o'
                                estado_triqui[2][1] = 'O'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif y < 150 and x < 150:                       # ABAJO Y DERECHA
                        if estado_triqui[2][2]==0:
                            circulo(2,2)
                            print(f"Turno # {cox} Turno de CIRCULO O")
                            print("izquierda")
                            if confirmador.value():
                                confirmador.value(1)
                                print("sisi")
                                bandera_9[0] = True
                                bandera_9[1] = 'o'
                                estado_triqui[2][2] = 'O'
                                cox+=1
                                print(estado_triqui)
                        else:
                            oled.text("OCUPADO", 35, 35, 0)
                            print("ocupado")
                    elif confirmador.value():
                        confirmador.value(1)
                        cox+=1
                        print(f"Cambio de turno {cox}")

            if valida_ganador(estado_triqui)== 'EMPATE':
                oled.text("EMPATE", 35, 35, 0)
                cont+=1
                print(cont)
            if valida_ganador(estado_triqui) != 0 and not valida_ganador(estado_triqui)== 'EMPATE' :
                val_fin = True
                cont+=1
                print(cont)
                cadena = "EL GANADOR ES " + valida_ganador(estado_triqui)             
            oled.text(cadena, 0, 35, 0)
            
            
                
                

            if cont==20:
                break
                
                
            #if cadena != "":
                #if confirmador.value():
                    #sleep_ms(1000)      
                    #confirmador.value(1)
                    #break              
                           
            oled.show()
            sleep_ms(100)
            oled.fill(0)

    oled.show()
    sleep_ms(200)
    oled.fill(0)
