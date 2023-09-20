# Ejercicio del Perimetro de un cuadrado
# Formula del perimetro del cuadrado
# p = l*4


def calcular_perimetro_cuadrado(lado):
    perimetro = lado * 4
    return(perimetro)

# Solicitar al usuario cuando mide uno de los lados del cuadrado
lado = float(input("Ingrese cuanto mide uno de los lados del cuadrado: "))

# Calcular el perimetro utilizando la función
perimetro = calcular_perimetro_cuadrado(lado)

# Mostrar el resultado
print(f"El perimetro del cuadrado con lado {lado} es: {perimetro}")

