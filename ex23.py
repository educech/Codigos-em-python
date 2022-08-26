
n = str(input("Digite um numero de 0 a 9999\n"))
q = len(n)#QUANTIDADE DE NUMEROS
print(f"Analisando o numero {n}.........")
if q==1:
    print(f"unidade: {n}")
elif q==2:
    print(f"dezena {n[0]}\nunidade {n[1]}")
elif q==3:
    print(f"centena: {n[0]}\ndezena: {n[1]}\nunidade: {n[2]}")
elif q==4:
    print(f"milhar: {n[0]}\ncentena: {n[1]}: \ndezena: {n[2]}\nunidade: {n[3]}")
elif q>=5:

    print(f"POR FAVOR, DIGITE UM NÚMERO DE 0 A 9999")