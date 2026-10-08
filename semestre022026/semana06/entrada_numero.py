# Direitos Autorais 2020, Universidade Brigham Young-Idaho. Todos os direitos reservados.

"""Este módulo contém duas classes, EntradaInteiro e EntradaDecimal, que permitem
um usuário inserir um número inteiro ou um número decimal em um widget
Entry do tkinter.
"""
import tkinter as tk
from tkinter import Entry
from numbers import Number
from sys import float_info


class _EntradaNumerica(Entry):
    _ESTILO_ERRO = {"bg": "pink", "fg": "black"}

    def __init__(self, pai, tipo_dado, nome_dado,
                 limite_minimo, limite_maximo, padrao, argumentos):
        super().__init__(pai)

        assert type(self) != _EntradaNumerica, \
            "não é possível criar um objeto _EntradaNumerica; " \
            "somente classes filhas de _EntradaNumerica podem ser instanciadas"
        assert isinstance(limite_minimo, tipo_dado), \
            f"limite_minimo deve ser " + nome_dado
        assert isinstance(limite_maximo, tipo_dado), \
            f"limite_maximo deve ser " + nome_dado
        assert limite_minimo < limite_maximo, \
            "limite_minimo deve ser menor que limite_maximo"

        self.__tipo_dado = tipo_dado
        self.__nome_dado = nome_dado
        self.__limite_minimo = limite_minimo
        self.__limite_maximo = limite_maximo

        if padrao is not None:
            assert isinstance(padrao, tipo_dado), \
                f"padrao deve ser " + nome_dado
            assert self._dentro_dos_limites(padrao), \
                "padrao deve estar entre limite_minimo e limite_maximo"
            self.delete(0, tk.END)
            self.insert(0, str(padrao))

        self.__definir_argumentos_tk(argumentos)
        self.bind("<FocusIn>", _EntradaNumerica.__selecionar_tudo)

    def __definir_argumentos_tk(self, argumentos):
        """Define os argumentos utilizados pelo tkinter."""
        if "justify" not in argumentos:
            argumentos["justify"] = "right" # alinhamento à direita
        if "width" not in argumentos:
            argumentos["width"] = max(
                len(str(self.__limite_minimo)), len(str(self.__limite_maximo)))
        argumentos["validate"] = "focusin"
        argumentos["validatecommand"] = (
            self.register(self.__validar_tudo), "%V", "%s", "%P")
        self.config(**argumentos)
        self._estilo_original = {"bg": self["bg"], "fg": self["fg"]}

    @staticmethod
    def __selecionar_tudo(evento):
        """Seleciona todos os caracteres no campo de entrada."""
        entrada = evento.widget
        entrada.select_range(0, tk.END)
        entrada.icursor(tk.END)

    @staticmethod
    def _contem_espaco(texto):
        return any(c.isspace() for c in texto)

    def __validar_tudo(self, motivo, texto_atual, texto_permitido):
        valido = False
        if motivo == "key":
            valido = self._validar_tecla(texto_atual, texto_permitido)
        elif motivo == "focusin":
            valido = self.__foco_entrada(texto_atual)
        elif motivo == "focusout":
            valido = self.__foco_saida(texto_atual)
        return valido

    def __foco_entrada(self, texto_atual):
        self.config({"validate": "all"})
        return self.__validar_foco(texto_atual)

    def __foco_saida(self, texto_atual):
        self.config({"validate": "focusin"})
        return self.__validar_foco(texto_atual)

    def __validar_foco(self, texto_atual):
        valido = False
        try:
            numero = self._converter(texto_atual)
            valido = self._dentro_dos_limites(numero)
        except ValueError:
            pass
        estilo = self._estilo_original if valido else _EntradaNumerica._ESTILO_ERRO
        self.config(estilo)
        return valido

    def _dentro_dos_limites(self, numero):
        return self.__limite_minimo <= numero <= self.__limite_maximo

    def definir(self, numero):
        """Exibe um número para o usuário."""
        assert isinstance(numero, self.__tipo_dado), \
            "numero deve ser " + self.__nome_dado
        assert self._dentro_dos_limites(numero), \
            f"numero deve estar entre {self.__limite_minimo} e {self.__limite_maximo}"
        self.delete(0, tk.END)
        self.insert(0, str(numero))

    def obter(self):
        """Retorna o número digitado pelo usuário."""
        numero = self._converter(super().get())
        if not self._dentro_dos_limites(numero):
            raise ValueError("número deve estar entre"
                             f" {self.__limite_minimo} e {self.__limite_maximo}")
        return numero

    def limpar(self):
        self.config({"validate": "focusin"})
        self.config(self._estilo_original)
        self.delete(0, tk.END)


class EntradaInteiro(_EntradaNumerica):
    """Um campo Entry que aceita apenas números inteiros entre
    um limite minimo e maximo opcionais.
    """
    def __init__(self, pai, *, limite_minimo=-2**63,
                 limite_maximo=2**63 - 1, padrao=None, **argumentos):
        super().__init__(pai, int, "um inteiro",
                         limite_minimo, limite_maximo, padrao, argumentos)

        self.__entrada_minimo = limite_minimo if limite_minimo <= 1 else 1
        self.__entrada_maximo = limite_maximo if limite_maximo >= -1 else -1
        self.__permite_negativo = (limite_minimo < 0)

    def _validar_tecla(self, texto_atual, texto_permitido):
        permitido = valido = False
        try:
            if not _EntradaNumerica._contem_espaco(texto_permitido):
                numero = int(texto_permitido)
                permitido = self.__entrada_minimo <= numero <= self.__entrada_maximo
                if permitido:
                    valido = self._dentro_dos_limites(numero)
        except ValueError:
            permitido = (len(texto_permitido) == 0 or
                         (self.__permite_negativo and texto_permitido == "-"))

        if not permitido:
            try:
                numero = int(texto_atual)
                valido = self._dentro_dos_limites(numero)
            except ValueError:
                pass

        estilo = self._estilo_original if valido else _EntradaNumerica._ESTILO_ERRO
        self.config(estilo)
        return permitido

    @staticmethod
    def _converter(texto): return int(texto)


class EntradaDecimal(_EntradaNumerica):
    """Um campo Entry que aceita apenas números decimais entre
    um limite minimo e maximo opcionais.
    """
    def __init__(self, pai, *, limite_minimo=-float_info.max,
                 limite_maximo=float_info.max, padrao=None, **argumentos):
        super().__init__(pai, Number, "um número",
                         limite_minimo, limite_maximo, padrao, argumentos)

        if limite_minimo < 0:
            self.__entrada_minimo = limite_minimo
        elif limite_minimo < 1:
            self.__entrada_minimo = 0
        else:
            self.__entrada_minimo = 1

        if limite_maximo <= -1:
            self.__entrada_maximo = -1
        elif limite_maximo <= 0:
            self.__entrada_maximo = 0
        else:
            self.__entrada_maximo = limite_maximo

        self.__permite_negativo = (limite_minimo < 0)
        self.__permite_ponto_inicial = (
            (-1 < limite_minimo < 1) or
            (-1 < limite_maximo < 1) or
            (limite_minimo <= -1 and 1 <= limite_maximo))

    def _validar_tecla(self, texto_atual, texto_permitido):
        permitido = valido = False
        try:
            if not _EntradaNumerica._contem_espaco(texto_permitido):
                numero = float(texto_permitido)
                permitido = self.__entrada_minimo <= numero <= self.__entrada_maximo
                if permitido:
                    valido = self._dentro_dos_limites(numero)
        except ValueError:
            permitido = (len(texto_permitido) == 0 or
                         (self.__permite_negativo and texto_permitido == "-") or
                         (self.__permite_ponto_inicial and texto_permitido == ".") or
                         (self.__permite_negativo and self.__permite_ponto_inicial
                          and texto_permitido == "-.")
                         )

        if not permitido:
            try:
                numero = float(texto_atual)
                valido = self._dentro_dos_limites(numero)
            except ValueError:
                pass

        estilo = self._estilo_original if valido else _EntradaNumerica._ESTILO_ERRO
        self.config(estilo)
        return permitido

    @staticmethod
    def _converter(texto): return float(texto)
