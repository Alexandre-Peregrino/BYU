with open('sistema_rh.txt', encoding='utf-8') as pessoal:
    next(pessoal)
    for pessoa in pessoal:
        linha_limpa = pessoa.strip()          # remove \n e espaços das pontas
        parte = linha_limpa.split()
        nome = parte[0]
        id = parte[1]
        profissao = parte[2]
        salario = float(parte[3]) / 24

        if profissao == "Engenheiro(a)":
            salario = salario + 1000

        valor = f'{salario:,.2f}'
        valor_br = valor.replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f'{nome} (ID: {id}), {profissao} - R$ {valor_br}')