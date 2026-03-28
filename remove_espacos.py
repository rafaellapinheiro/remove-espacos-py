texto = input("Digite uma frase: ")
lista = list(texto)

while lista and lista[0] == " ":
    lista.pop(0)

while lista and lista[-1] == " ":
    lista.pop()

resultado = "".join(lista)

print("Resultado:", resultado)
