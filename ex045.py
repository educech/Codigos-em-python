from random import randint
from time import sleep
item = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)##DESSA FORMA JA FIZ A JOGADA DO COMPUTADOR
print('''SUAS OPÇÕES
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("QUAL A SUA JOGADA?\n"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÓ")
sleep(1)
if jogador == 0 and computador == 2:
    print("VOCÊ VENCEU!!")
elif jogador == 1 and computador == 0:
    print("VOCÊ VENCEU!!")
elif jogador == 2 and computador == 1:
    print("VOCÊ VENCEU!!")
elif jogador == computador:
    print("EMPATE")
elif jogador >= 3:
    print("JOGADA INVÁLIDA")
else:
    print("VOCÊ PERDEU!!")
print("-=" * 20)
print(f'''Você jogou:{(item[jogador])}
computador jogou:{(item[computador])}''')
print("-="* 20)







