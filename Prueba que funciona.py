from math import acos, cos, sin
from math import radians
from turtle import pen

a=0
while a!=2:
    menu=int(input("1.- Registrarse\n2.-Comenzar carrera\n"))
    i=1 
    auto="Apagado"
    velocidad=0
    if menu ==1 and a==0:
        cantidad=int(input("¿Cuantos autos desa ingresar?\n"))
        b=1
        chofer=[cantidad]
        rut=[cantidad]
        modelo=[cantidad]
        patente=[cantidad]  
        while b<=cantidad:
            chofer.append(input("Ingrese el nombre y apellido del conductor Nº"+str(b)+"\n"))
            rut.append(input("Ingrese el rut del chofer\n"))
            modelo.append(input("Ingrese el modelo del auto\n"))
            patente.append(input("Ingrese la patente del auto\n"))
            b=b+1
            a=1
    else:
        print("Debe registrarse primero")      
    if menu == 2 and a==1:
        c=int(input(print("Ingrese el auto que ralizara la carrera")))
        slon=radians(int(input("Ingrese la longitud de destino\n")))
        slat=radians(int(input("Ingrese la latitud de destino\n")))
        elon=radians(int(input("Ingrese la longitud inicio\n")))
        elat=radians(int(input("Ingrese la latitud inicio\n")))
        
        while i!=0:
            if menu == 2:
                print("1.-Encender auto\n2.-Acelerar\n3.-Frenar\n4.-Apagar auto\n5.-Salir\n6.-Ver Feha\n7.-Mostrar datos\n")    
                menu2=int(input("Ingrese opcion\n"))
            if menu2 == 1:
                auto="Encendido"
                print("Auto encendido")
            if menu2 == 2:
                if auto != "Encendido":
                    print("No se puede acelerar, auto apagado")
                else:
                    velocidad+=10
                    print("Velocidad actual: ",velocidad,"km/h")
            if menu2 == 3:
                if velocidad==0:
                    print("Ya estas detenido")
                else:
                    velocidad=velocidad-10
                    print("viajas a ",velocidad," km/h")
            if menu2 == 4:
                if velocidad !=0:
                    print("No puedes apagar el auto en movimiento")
                else:
                    auto="Apagado"
                    print("Auto apagado")
            if menu2 == 5:
                if velocidad > 0:
                    print("Saliste del auto mientras estaba en movimiento, deberias llamar una ambulancia")
                else:
                    print("Saliste del auto")
                i=0
                a=2
            if menu2 == 6:
                import datetime
                print(datetime.datetime.now())
            if menu2 == 7:
                print("Nombre: ",chofer[c],"\nRut: ",rut[c],"\nModelo: ",modelo[c],"\nPatente: ",patente[c])
        dist=6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
        d=round(dist,2)
        pago=dist*450
        p=round(pago,2)
        print("Distancia recorrida: ",d,"km\nMonto a pagar: $",p)
