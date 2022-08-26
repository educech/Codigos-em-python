
print('''\nExercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos: APOS A SOPA A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
''')

##COM O FOR
'''frase = str(input("Digite uma frase:\n")).strip().upper()##Aqui ja tirou os espaços e colocou tudo maiuscula
palavras = frase.split()##separa a frase em palavras
junto = ''.join(palavras) ##junta todas as palavras
inverso = ''##vazio no início
for letra in range (len(junto) -1, -1, -1):  ##colocar a frase de tras para frente
    inverso += junto[letra]
print(f"O inverso de \033[31m{junto} é {inverso}")
if junto == inverso:
    print("\033[mÈ UM PALÍNDROMO")
else:
    print(("\033[mNÃO É UM PALÍNDROMO"))'''

##SEM O FOR

frase = str(input("Digite uma frase:\n")).strip().upper()##Aqui ja tirou os espaços e colocou tudo maiuscula
palavras = frase.split()##separa a frase em palavras
junto = ''.join(palavras) ##junta todas as palavras
inverso = junto[::-1]
print(f"O inverso de \033[31m{junto} é {inverso}")
if junto == inverso:
    print("\033[mÈ UM PALÍNDROMO")
else:
    print(("\033[mNÃO É UM PALÍNDROMO"))
