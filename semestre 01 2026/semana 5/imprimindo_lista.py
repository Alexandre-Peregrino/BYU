#Imprimindo lista na mesma linha separados por vírgula

livros = []

livros.append("1 Néfi")
livros.append("2 Néfi")
livros.append("Jacó")
livros.append("Enos")

print("Seus livros são:")

print(*livros, sep=", ")