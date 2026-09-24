def exibir_regular(texto_usuario):
    print(f'O texto digitado foi: {texto_usuario}')
    return texto_usuario

def exibir_maiuscula(texto_usuario):
    print(f'O texto maiúsculo é: {texto_usuario}'.upper())
    return texto_usuario

def exibir_minuscula(texto_usuario):
    print(f'O texto minúsculo é: {texto_usuario}'.lower())
    return texto_usuario

texto_usuario = input("Digite um texto: ")
exibir_regular(texto_usuario)  
exibir_maiuscula(texto_usuario)
exibir_minuscula(texto_usuario)