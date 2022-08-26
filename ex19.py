'''import random
n1 = input(str("Digite o nome do primeiro aluno: "))
n2 = input(str("Digite o nome do segundo aluno: "))
n3 = input(str("Digite o nome do terceiro aluno: "))
n4 = input(str("Digite o nome do quarto aluno: "))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f"O aluno escolhido foi {escolhido}")'''

from random import choice
n1 = input(str("Digite o nome do primeiro aluno: "))
n2 = input(str("Digite o nome do segundo aluno: "))
n3 = input(str("Digite o nome do terceiro aluno: "))
n4 = input(str("Digite o nome do quarto aluno: "))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f"O aluno escolhido foi {escolhido}")