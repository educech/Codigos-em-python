'''cont = 0
soma = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
       cont = cont + 1
       soma = soma + c
print(f"A soma de todos os {cont} valores é igual a {soma}")'''

cont = 0
soma = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
       cont += 1
       soma += c
print(f"A soma de todos os {cont} valores é igual a {soma}")