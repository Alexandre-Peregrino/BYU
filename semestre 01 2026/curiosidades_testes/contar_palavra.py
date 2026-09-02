from pypdf import PdfReader

# 1. Abrir o PDF
leitor = PdfReader('livro_de_mormom.pdf')

# 2. Extrair o texto de todas as páginas
texto = ""
for pagina in leitor.pages:
    texto += pagina.extract_text() + " "

# 3. Limpar: minúsculas + remover pontuação
texto_limpo = texto.lower()
for pontuacao in [',', '.', ';', ':', '!', '?', '"', "'", '(', ')', '-', '—']:
    texto_limpo = texto_limpo.replace(pontuacao, ' ')

# 4. Quebrar em palavras e contar
palavras = texto_limpo.split()
palavra_alvo = 'jesus cristo',
quantidade = palavras.count(palavra_alvo)

print(f'A palavra "{palavra_alvo}" aparece {quantidade} vezes no livro')
print(f'O livro tem {len(palavras)} palavras no total')