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
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

def numeros():
    print("A continuación, ingrese 3 números enteros:")
    global numero_1, numero_2, numero_3 
    numero_1 = input()
    numero_2 = input()
    numero_3 = input()
    try:
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
        numero_3 = int(numero_3)
    except: 
        print("Vuelva a intentar ingresar su números. Asegúrese de que sean enteros y no decimales o letras")
        numeros()
        
numeros()

if (numero_1 % 2) == 0:
    print(numero_1, "es par.")
else:
    print(numero_1, "es impar.")

if (numero_2 % 2) == 0:
    print(numero_2, "es par.")
else:
    print(numero_2, "es impar.")

if (numero_3 % 2) == 0:
    print(numero_3, "es par.")
else:
    print(numero_3, "es impar.")
    
