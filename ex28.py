from random import randint #randomizar

from time import sleep # faz esperar alguns segundos

c = randint(0,5)## faz o  computador pensar e randomiza o numero de 0 a 5

print("-=-" * 20)
print(f"Vou pensar em um numero de 0 a 5, tente adivinhar ")
print("-=-" * 20)
j = int(input("em que número eu pensei:\n"))#faz o jogador pensar
print("PROCESANDO.....")

sleep(3)

if j>5:  # aqui o usuario que digitar um numero que não esteja entre 0 e 5 não rodara da maneira correta
    print("Por favor digite um numero de que esteja entre 0 e 5")

elif c==j:
    print(f"Eu pensei no número {c}, parabéns você acertou")

elif c!=j: # (!=) equivale ao sinal de diferente
    print(f"Eu pensei no numero {c}, você errou")









