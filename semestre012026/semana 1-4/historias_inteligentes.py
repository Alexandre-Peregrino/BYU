# print('Por favor, digite o seguinte: ')

# adjetivo = input('adjetivo: ')
# animal = input('animal: ')
# verbo1 = input('verbo: ')
# exclamacao = input('exclamação: ')
# verbo2 = input('verbo: ')
# verbo3 = input('verbo: ')

# print(f'''Outro dia, eu estava realmente em apuros. Tudo começou quando eu vi um {animal} {adjetivo} {verbo1} pelo corredor. Eu gritei "{exclamacao.capitalize()}!". Mas tudo que eu conseguia pensar em fazer era {verbo2} repetidamente. Milagrosamente,
# isso fez com que ele parasse, mas não antes de tentar {verbo3} bem na frente da minha família.''')



# Adição Criativa: O programa agora ajusta automaticamente o artigo (um/uma) com base no gênero do animal e formata as entradas para garantir fluidez no texto.

print('************************************')
print('*      GERADOR DE HISTÓRIAS        *')
print('************************************')
print('\nPor favor, digite o seguinte:\n')

# Entradas básicas
adjetivo = input('Adjetivo: ').lower()
animal = input('Animal: ').lower()
genero = input('O animal é masculino ou feminino? (m/f): ').lower()
lugar = input('Um lugar (ex: quartel, parque): ').lower()
verbo1 = input('Verbo no gerúndio (ex: correndo): ').lower()
exclamacao = input('Exclamação: ')
verbo2 = input('Verbo no infinitivo (ex: pular): ').lower()
verbo3 = input('Outro verbo no infinitivo: ').lower()

# Lógica Criativa: Ajuste de artigo definido/indefinido
artigo = 'um' if genero == 'm' else 'uma'

print('\nGerando sua história...')
print('-' * 50)

# História expandida com f-string
print(f'''
Outro dia, eu estava realmente em apuros no {lugar}. 
Tudo começou quando eu vi {artigo} {animal} {adjetivo} {verbo1} pelo corredor. 
Eu gritei "{exclamacao.capitalize()}!". 

Mas tudo que eu conseguia pensar em fazer era {verbo2} repetidamente. 
Milagrosamente, isso fez com que o animal parasse, mas não antes de 
tentar {verbo3} bem na frente da minha família.
''')

print('-' * 50)
