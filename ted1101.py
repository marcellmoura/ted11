VET = []

for i in range(10):
    num = int(input(f"Digite o número {i + 1}: "))
    VET.append(num)

repetidos = {}
for i in range(len(VET)):
    if VET.count(VET[i]) > 1:
        if VET[i] not in repetidos:
            repetidos[VET[i]] = []
        repetidos[VET[i]].append(i)

if repetidos:
    print("Números repetidos e suas posições:")
    for numero, posicoes in repetidos.items():
        print(f"Número {numero} encontrado nas posições: {posicoes}")
else:
    print("Não existem números repetidos no vetor.")