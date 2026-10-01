#https://github.com/SofiLMM/Proyecto-Messanimal-
import random

def datos():
    #Pide pensaje, destino, direccion, fecha y hora del envio
    destinatario = input("Nombre del destinatario:")
    direccion = input("Direecion del destinatario:")
    mensaje = input("Escribe el mensaje:")
    fecha_hora = int(input("Fecha y hora del envio (dia/mes/año 00:00):"))

    return destinatario, direccion, mensaje, fecha_hora

def animales():
    #Se muestran los animales disponibles
    print("Animales disponibles: Paloma, tortuga, caracol, aguila, colíbri, hormiga, oruga")
    animal= input("Elige un animal: ")
    
    return animal

def confirmacion():
    #Esto es para conirmas el envio del mensaje, se mete un while para validar la respuesta
    #devolviendo un true o false
    while True:
        respuesta= input("¿Confirmar el envio? (si/no):").lower()
        match respuesta:
            case "si":
                return True
            case "no":
                return False
            case _:
                print("Solo responde (si) o (no)")
                
#Aqui ya con los datos vamos ir haciendo las acciones que se deben
def obtener_distancia(direccion):
    #Esta funcion esta pendiente porque no se como obtener los km
    #Porque puedo pedirlo directamente pero sería demasiado sencillo
    #O puedo hacer un menu con las opciones de distancia
def tiempo_viaje(distancia, animal):
    #Calcula cuanto tiempo tarda el animal en recorrer la distancia
    velocidad= #aqui iria la velocidad promedio de cada animal
    horas_exactas= distancia/velocidad
    return horas_exactas

def hora_llegada(fecha_hora, distancia, animal):
    horas_viaje= tiempo_viaje(distancia, animal)
    return horas_viaje, fecha_hora #Falta calcular la fecha exacta y hora en la que llegaria
    #aun no se como calcularlo

def estatus_animal():
    #Se pone aleatoriamnete eventos que le puede suceder al animal durante el trayecto
    return random.choice(se murio, se lo comieron, choco, se detuvo a comer)

def notificacion(estatus_animal, destinatario):
    #Dependiendo del estatus del animal se le notifica al usuario si llego el mensaje o no
    if estatus_animal:
        return print("No entregado, el animalito {estatus_animal}")
    else:
        return print("El mensaje llego con exito a {destinatorio}")

def main():
    while True:
        destinatario, direccion, mensaje, fecha_hora = datos()
        animal = animales()
        
        if confirmacion():
            print("Mensaje confirmado, enviando...")
            break
        else:
            print("Envio cancelado")
    distancia = obtener_distancia(direccion)
    
    if distancia is None:
        print("#Aqui falta si se puede hacer directo o se debe de poner un menu ya predeterminado")
        
        return
    
    estado_animal= estatus_animal()
    noti= notificacion(estatus_animal, destinatario)
    llega= hora_llegada(fecha_hora, distancia, animal)
    
    print("Estatus del animal: {estatus_animal}")
    print("Estatus de envio: {hora_llegada}")
    print("Mnesaje de confirmacion: El mensaje para {destinatario} fue enviado con {animal}")
    print("Notificacion final: {noti}")
    
main()