movieName = "Top Gun"
movieDescription = """
    Top Gun Maverick, é um filme de aviação e aventura,
muito consagrado na indústria
"""
print(movieName.join("-"))  # junta os caracteres da string com um separador
print(movieName.upper())  # tudo maiúsculo
print(movieName.lower())  # tudo minúsculo
print(movieName.capitalize())  # primeira letra maiúscula
print(movieName.title())  # primeira letra de cada palavra maiúscula
print(movieName.center(10, '-'))  # centraliza a string com um preenchimento
# retorna a posição de um determinado caractere ou substring
print(movieName.find("u"))
print(movieName.find("o"))  # conta caracteres
print(movieName.replace("Top", "Matrix"))  # substitui um caractere por outro
print(movieName.split())  # divide a string em uma lista de palavras
print(movieDescription.splitlines())  # divide a string em uma lista de linhas
# remove espaços em branco no início e no final da string
print(movieName.strip())
# verifica se a string começa com um determinado prefixo
print(movieName.startswith("Top"))
# verifica se a string termina com um determinado sufixo
print(movieName.endswith("Gun"))
print(movieName.isalpha())  # verifica se a string contém apenas letras
print(movieName.isdigit())  # verifica se a string contém apenas dígitos
# verifica se a string contém apenas letras e dígitos
print(movieName.isalnum())
