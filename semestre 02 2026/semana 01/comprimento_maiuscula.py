#Exemplo 6
# Obtém uma string do usuário.
texto1 = input("Digite uma frase motivacional: ")
# Chama a função embutida len para obter
# o número de caracteres no texto.
comprimento = len(texto1)
# Chama o método string upper para converter
# texto1 em letras maiúsculas.
texto2 = texto1.upper()
# Chama a função embutida print para exibir
# o comprimento do texto e o texto em
# letras maiúsculas para o usuário ver.
print(comprimento, texto2)

print(dir(__builtins__)) #Retorna uma lista de todas as funções embutidas disponíveis
help() #Retorna a documentação de todas as funções embutidas disponíveis