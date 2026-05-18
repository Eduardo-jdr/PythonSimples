filmTheCloverfieldParadox = [
    "The Cloverfield Paradox",
    "Actors: Daniel Brühl, Elizabeth Debicki, Gugu Mbatha-Raw",
    "Release Year: 2018",
    "Genre: Science Fiction, Horror",
    "Rating: 5.4/10"]

# Tamanho da lista
print(len(filmTheCloverfieldParadox))

# Acessando elementos da lista
print(filmTheCloverfieldParadox[0])  # Título do filme
print(filmTheCloverfieldParadox[1])  # Atores
print(filmTheCloverfieldParadox[2])  # Ano de lançamento
print(filmTheCloverfieldParadox[3])  # Gênero
print(filmTheCloverfieldParadox[4])  # Avaliação

# Modificando um elemento da lista
filmTheCloverfieldParadox[4] = "Rating: 6.0/10"
print(filmTheCloverfieldParadox[4])  # Avaliação atualizada
# Imprime a lista completa com a avaliação atualizada
print(filmTheCloverfieldParadox.index(
    "Genre: Science Fiction, Horror"))  # Índice do gênero
# Adiciona o diretor à lista
print(filmTheCloverfieldParadox.append("Director: Julius Onah"))
# Imprime a lista completa com o diretor adicionado
print(filmTheCloverfieldParadox)

# Faz uma cópia da lista
filmTheCloverfieldParadoxCopy = filmTheCloverfieldParadox.copy()
# Remove a avaliação original da lista
filmTheCloverfieldParadox.remove("Rating: 6.0/10")
print(filmTheCloverfieldParadox)  # Imprime a lista sem a avaliação
# remove todos os itens da lista
filmTheCloverfieldParadox.clear()
print(filmTheCloverfieldParadox)  # Imprime a lista vazia
# Imprime a cópia da lista original, que ainda contém os itens
print(filmTheCloverfieldParadoxCopy)
