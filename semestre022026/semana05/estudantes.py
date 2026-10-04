import csv
import subprocess

def ler_dicionario(arquivo_csv, indice_id=0):
    estudantes = {}
    with open(arquivo_csv, 'rt', encoding='utf-8') as arquivo_de_estudantes:
        leitor_de_arquivo = csv.reader(arquivo_de_estudantes)
        next(leitor_de_arquivo)  # pula o cabeçalho
        for linha in leitor_de_arquivo:
            if len(linha) >= indice_id + 2:
                estudantes[linha[indice_id]] = linha[indice_id + 1]
    return estudantes

def main():
    subprocess.run(['clear'])

    d_estudante = ler_dicionario('estudantes.csv')

    id_estudante = input("Digite o ID do estudante: ")
    id_estudante = id_estudante.replace("-", "")
    if id_estudante in d_estudante:
        print(f"Nome do estudante: {d_estudante[id_estudante]}")
    elif not id_estudante.isdigit():
        print("ID inválido. Digite apenas números.")
    elif len(id_estudante) < 9:
        print("ID inválido. Digitos insuficientes.")
    elif len(id_estudante) > 9:
        print("ID inválido. Digitos excedentes.")
    else:
        print("Estudante inexistente.")

if __name__ == "__main__":
    main()