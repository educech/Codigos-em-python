from datetime import date
ano = int(input("Digite o ano de nascimento do aluno:\n"))
atual = date.today().year
idade =  atual - ano
print(f"O atleta tem {idade} anos")
if idade <= 9:
    print("Classificação : MIRIM")
elif idade <= 14:
    print("Classificação : INFANTIL")
elif idade <= 19:
    print("Classificação : JUNIOR")
elif idade <= 25:
    print("Classificação : SÊNIOR")
else:
    print("Classificação : MASTER")




