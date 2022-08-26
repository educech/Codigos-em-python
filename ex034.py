s = float(input("Digite o valor do salário:\n"))
if s <= 1250:
   novo = (s + s * 15/100)
else:
    novo = (s + s * 10/100)
print(f"Quem ganhava {s} R$ passara a ganhar {novo:.2f} R$")