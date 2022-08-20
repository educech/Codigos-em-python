from random import randint

n = randint(1, 10)

palpite = int(input("Digite um número: "))

while palpite != n:
    print(f"TENTE NOVAMENTE!!")
    palpite = int(input("Digite um número: "))

print(f"Você acertou o numero sorteado foi {n}")
