'''d = float(input("Digite a distancia da viagem:\n"))
p = (d * 0.50)
t = (d * 0.45)        ## valor com desconto
print(f"voçê esta prestes a começar uma viagem de {d}Km")
if d<=200:
    print(f"Sua viagem custara {p:.2f} R$")
else:
    print(f"Sua vaigem custará {t:.2f} R$")'''

d = float(input("Digite a distancia da viagem:\n"))
print(f"voçê esta prestes a começar uma viagem de {d}Km")
p = d * 0.50 if d <= 200 else d * 0.45 ###fFORMA DIFERENTE DE USAR O IF E O ELSE
print(f"O preço da sua passagem custará {p}:\n")