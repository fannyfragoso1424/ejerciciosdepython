# Pedir al usuario que ingrese elementos separados por comas y crear una lista
entrada_usuario = input("Igresa los elementos de la lista separados por comas: ")
elementos= entrada_usuario.split(',')

# Invertir la lista utilizando la técnica de rebanado de pizzas (slicing)
lista_invertida = elementos[::-1]

# Mostrar la lista invertida
print("Lista invertida:", lista_invertida)


