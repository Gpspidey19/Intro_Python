#ejercicio1 For
#coleccion = {"Gp":22,"Spiderman":20,"Avengers":13}
#for clave,valor in coleccion.items():
#    print(f"{clave} -> {valor}")


#Ejercicio2-Intro
# a = int(input("Ingrese a->"))
# b = int(input("Ingrese b->"))
# suma=a+b
# print(f"La respuesta es {suma}")


#Intercambiar el valor entre 2 variables
# a = int(input("Ingrese a->"))
# b = int(input("Ingrese b->"))
# a,b=b,a
# print(f"valor de a-> {a}")
# print(f"valor de b-> {b}")


#Intercambiar el valor entre 3 variables
# a = int(input("Ingrese a->"))
# b = int(input("Ingrese b->"))
# c= int(input("Ingrese c->"))
# a,b,c=c,a,b
# print(f"valor de a-> {c}")
# print(f"valor de b-> {a}")
# print(f"valor de c-> {b}")


#Radio de circunferencia
# import math
# radio = float(input("Ingrese r ->"))
# longitud=2*math.pi*radio
# area=math.pi*radio*radio
# print(f"longitud -> {longitud}")
# print(f"area -> {area}")
# print("{0:.2f}".format(longitud)) #Para dos decimales


# #condicionales
# numero = int(input("ingrese un numero ->"))
# if numero>0:
#     print("Numero positivo")
# elif numero==0:
#     print("Numero es cero")
# else:
#     print("Numero negativo")


##condicionales multiples
# numero=int(input("Ingresa tu edad ->"))
# if numero>0:
#     if numero>=18 and numero<60:
#         input("Es mayor de edad")
#     elif numero>=60 and numero<105:
#         input("Es viejo")
#     elif numero>=105:
#         input("ERROR")
#     else:
#         input("Es menor de edad")
# elif numero==0:
#     print("Numero es cero")
# else:
#     input("El numero debe ser positivo")


#   a=int(input("a: "))
#   b=int(input("b: "))
#   if a%2==0 and b%2==0:
#       print("Ambos numeros son pares")
#   elif (a%2==0 and b%2!=0):
#       print(f"Par: {a}")
#   elif a%2!=0 and b%2==0:
#       print(f"Par: {b}")
#   else:
#       print("Ningún número es par")


# #Determinar si es una vocal o no
# letra=input("Ingrese una letra: ").lower() #Transforma la mayuscula a minuscula .... upper es para mayuscula a minuscula
# if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
#     print("Es una vocal")
# else:
#     print("NO es una vocal")


# #Calculadora  s r m d
# letra = input("Ingrese la operación: ").lower()
# if letra=='s':
#     s1=int(input("1er número: "))
#     s2=int(input("2do número: "))
#     print(s1+s2)
# elif letra=='r':
#     r1=int(input("1er número: "))
#     r2=int(input("2do número: "))
#     print(r1-r2)
# elif letra=='m':
#     m1=int(input("1er número: "))
#     m2=int(input("2do número: "))
#     print(m1*m2)
# elif letra=='d':
#     d1=int(input("1er número: "))
#     d2=int(input("2do número: "))
#     print(d1/d2)
# else:
#     print("Ingrese un caracter correcto")


# #Menu de opciones
# inicial=100
# letra=int(input("Ingrese la opción: "))
# if letra==1:
#     adicional=int(input("Monto adicional: "))
#     adicional+=inicial
#     print(f"Saldo actual: {adicional}")
# elif letra==2:
#     retiro=int(input("Monto a retirar: "))
#     if retiro>inicial:
#         print("Excede al saldo inicial")
#     else:
#         retiro=inicial-retiro
#         print(f"Saldo actual: {retiro}")
# elif letra==3:
#     print(f"Saldo actual: {inicial}")


#Listas
