#Definir dimensiones 
ancho = 5
alto = 6

#calcular area
area = ancho * alto

#calcular promedio
perimetro = 2 * (ancho + alto)

#mostrar resultados 
print ("area:", area)
print ("perimetro:", perimetro)

#edad coversion: ERROR (str * int no funciona con años )
edad = input ("¿cuantos años tienes?")
dias = int (edad) * 365
print("has vivido " + str(dias) + " dias" )
