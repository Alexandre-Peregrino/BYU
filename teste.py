<<<<<<< Updated upstream
metais={ "Ag" : "Prata", "Al": "Alumínio", "Au": "Ouro", "Fe": "Ferro", } 


print(metais["Au"])

if "Prata" in metais:
    print('ok')
    =======
def main():
    estudantes = {
        "42-039-4736": "Carlos Silva",
        "61-315-0160": "Maria Oliveira",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "João Pereira",
        "07-103-5621": "Maria Oliveira",
        "81-298-9238": "Samanta Paz"
    }
    id = input('Digite o id do estudante: ')

    nome = estudantes.get(id)
    if nome:
        print(nome)
        estudantes.pop(id)
    else:
        print('Estudante inexistente!')

    for chave, valor in estudantes.items():
        print(chave, valor)
if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
