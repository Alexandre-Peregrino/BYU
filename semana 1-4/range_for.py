
#Brincando com range

inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
passo = int(input("Digite o passo: "))

for i in range(inicio, fim, passo):
    print(i)
    if i == (fim - passo):
        print(i + passo)

# for i in range(10):
#     print(i + 1)