# Exercício 1: nome invertido

# nome = input("Digite seu primeiro nome: ")
# sobrenome = input("Digite seu sobrenome: ")

# nomeInvertido = f"{sobrenome} {nome}"

# print(nomeInvertido)

# Exercício 2: Palavra palíndroma

# palavra = input("Digite uma palavra: ")

# if palavra == palavra[::-1]:
# print("A palavra é um palíndromo.")
# else:
# print("A palavra não é um palíndromo.")

# Exercício 3: Palíndromo 2

texto1 = "arara"
texto2 = "reviver"

texto1_formatado = texto1.replace(" ", "").lower()
texto2_formatado = texto2.replace(" ", "").lower()

palindromo1 = texto1_formatado == texto1_formatado[::-1]
palindromo2 = texto2_formatado == texto2_formatado[::-1]

print(f"{texto1} é um palíndromo? {palindromo1}")
print(f"{texto2} é um palíndromo? {palindromo2}")


# Exercício 4: texti invertido

# frase = "Meu nome é João"
# paragrafo = frase.split()
# fraseinvertida = " ".join(paragrafo[::-1])
# print(fraseinvertida)

# Exercício 5: Lista

# ler 3 números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Armazenar os números em uma lista
numeros = [num1, num2, num3]

# Imprimir a lista completa
print("Lista completa:", numeros)

# Imprimir o primeiro elemento da lista
print("Primeiro elemento:", numeros[0])

# Imprimir a soma de todos os elementos da lista
print("Soma dos elementos:", sum(numeros))
