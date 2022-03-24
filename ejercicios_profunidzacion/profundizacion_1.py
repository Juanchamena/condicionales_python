# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

def datos():
    global numero_1
    global numero_2
    numero_1 = input("Ingrese un número cualquiera: ")
    numero_2 = input("Ingrese otro número cualquiera: ")
    try:
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
    except:
        print("Vuelva a intentar.")
        datos()

datos()

diferencia = numero_1 - numero_2
if diferencia > 0:
    print("El resultado de la diferencia de los números ingresados es positivo")
elif diferencia < 0:
    print("El resultado de la diferencia de los número ingresados es negativo")
else:
    print("El resultado de la diferencia de los números ingresados es", diferencia)
#Horas buscando como usar una variable determinada dentro de una función, fuera de la función. 









        

