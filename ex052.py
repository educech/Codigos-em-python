
print('''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.\n''')


num = int(input("Digite um número\n"))
tot = 0 ##Total de números que foi divísivel
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=" ")
        tot += 1
    else:
        print('\033[31m', end=" ")
    print(c, end=" ")
print(f"\n\033[mO número {num} foi divisível {tot} vezes")
if tot == 2:## total de divisores, se for apenas 2 é primo, senão não é primo.
    print(f"E por isso ele É PRIMO")
else:
    print("Ele NÃO É PRIMO")