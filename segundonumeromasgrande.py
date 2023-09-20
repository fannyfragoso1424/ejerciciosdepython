# Ejercicio Encontrar el Segundo Número Más Grande en una Lista

#Se definen los pasos a seguir junto con las variables

def segundo_mas_grande(lista):
    if len(lista) <2:
        return "La lista debe contener al menos dos elementos"
    
    maximo = lista[0]
    segundo_maximo = lista[1]

    if segundo_maximo > maximo:
        maximo, segundo_maximo = segundo_maximo, maximo

    for elemento in lista[2:]:
        if elemento > maximo:
            segundo_maximo = maximo
            maximo = elemento
        elif elemento > segundo_maximo and elemento != maximo:
            segundo_maximo = elemento
    
    return segundo_maximo

#El ususario deberá escriri la lista de números

entrada = input("Ingrese la lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

#Se obtiene el resultado

resultado = segundo_mas_grande(numeros)
if isinstance(resultado, int):
    print(f"El segundo elemento más grande en la lista es: {resultado}")
else:
    print(resultado)