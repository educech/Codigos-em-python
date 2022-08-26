'''import random
n1 = input("Digite o numero do 1º aluno: ")
n2 = input("Digite o numero do 2º aluno: ")
n3 = input("Digite o numero do 3º aluno: ")
n4 = input("Digite o numero do 4º aluno: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print (f"A ordem de apresentação será")
print(lista)'''

from random import shuffle

n1 = input("Digite o numero do 1º aluno:\n ")
n2 = input("Digite o numero do 2º aluno:\n ")
n3 = input("Digite o numero do 3º aluno:\n ")
n4 = input("Digite o numero do 4º aluno:\n ")
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f"A ordem de apresentação será")
print(lista)


