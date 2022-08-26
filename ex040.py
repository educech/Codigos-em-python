n1 = float(input("Digite a primeira nota:\n"))
n2 = float(input("Digite a segunda nota:\n"))
m = (n1+n2)/2
if m >= 5 and m <= 6.9:
    print(f"Tirando {n1} e {n2} A média do aluno é {m} O aluno está de RECUPERAÇÃO")
elif m >= 7:
    print(f"Tirando {n1} e {n2} a média do aluno é {m} O aluno foi APROVADO")
else:
    print(f"Tirando {n1} e {n2} a média do aluno é {m} O aluno foi REPROVADO")
