c = float(input("Digite o valor da casa:\n"))
s = float(input("Salário do comprador:\n"))
a = int(input("Quantos anos de financiamneto:\n"))
m = (s * 30/100)
p = c/(a*12)
print(f"Para pagar uma casa de {c:.2f} R$ em {a} anos a prestação será de {p:.2f}")
if p <= m:
    print("Empréstimo ACEITO")
else:
    print("Emprestimo NEGADO")
