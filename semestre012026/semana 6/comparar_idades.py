pessoas = [
    ["Stephanie", 36],
    ["João", 29],
    ["Emília", 24],
    ["Graça", 54],
    ["Nícolas", 12],
    ["Penelope", 32],
    ["Miguel", 2],
    ["Jacó", 10]
]

# Encontrar pessoa mais jovem da lista

pessoa_mais_jovem = pessoas[0]

for pessoa in pessoas:
    print(pessoa, end=' ' )
    print(f'Nome: {pessoa[0]}, idade: {pessoa[1]}')
    if pessoa[1] < pessoa_mais_jovem[1]:
        pessoa_mais_jovem = pessoa
print()
print(f'A pessoa mais jovem é: {pessoa_mais_jovem[0]} com {pessoa_mais_jovem[1]} anos de idade')