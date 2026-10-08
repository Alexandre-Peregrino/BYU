import tkinter as tk
from tkinter import Frame, Label, Button
from entrada_numero import EntradaInteiro
import random

def main():
    raiz = tk.Tk()
    janela_principal = Frame(raiz)
    janela_principal.master.title("Lançamento de Dados")
    janela_principal.pack(padx=8, pady=8, fill=tk.BOTH, expand=1)
    configurar_janela(janela_principal)
    janela_principal.mainloop()

def configurar_janela(janela):
    rotulo_dados = Label(janela, text="Digite o número de lados dos seus dados (2-20)")
    rotulo_dados.grid(row=0, column=0)
    entrada_lados = EntradaInteiro(janela, limite_minimo=2, limite_maximo=20, width=4)
    entrada_lados.grid(row=0, column=1)

    rotulo_dados = Label(janela, text="Digite a quantidade de dados de lançamento (1-10)")
    rotulo_dados.grid(row=1, column=0)
    entrada_dados = EntradaInteiro(janela, limite_minimo=1, limite_maximo=10, width=4)
    entrada_dados.grid(row=1, column=1)

    botao_lancamento = Button(janela, text="Lance os Dados!")
    botao_lancamento.grid(row=2, column=0)

    botao_limpar = Button(janela, text="Limpar!")
    botao_limpar.grid(row=2, column=1)


    rotulo_resultado = Label(janela, text="")
    rotulo_resultado.grid(row=3, column=0)

    def lancamento(num_lados, qtd_dados):
        soma = 0
        texto_resultado = ""
        for lance in range(qtd_dados):
            aleatorio = random.randint(1, num_lados)
            soma += aleatorio
            texto_resultado = texto_resultado + f'{aleatorio}'
        texto_resultado = texto_resultado + f'| Total: {soma}'
        return texto_resultado

    def acao_limpar():
        entrada_lados.limpar()
        entrada_dados.limpar()
        rotulo_resultado.config(text="")
    botao_limpar.config(command=acao_limpar)

    def acao_botao():
        try:
            num_lados = entrada_lados.obter()
        except ValueError:
            rotulo_resultado.config(text="Digite um número de lados válido")
            return
        try:
            qtd_dados = entrada_dados.obter()
        except ValueError:
            rotulo_resultado.config(text="Digite uma quantidade lançamentos válido")
            return

        texto_resultado = lancamento(num_lados, qtd_dados)

        rotulo_resultado.config(text=texto_resultado)

    botao_lancamento.config(command=acao_botao)



if __name__ == '__main__':
    main()