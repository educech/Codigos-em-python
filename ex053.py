print("Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.\n\n")


from datetime import date ##importa a biblioteca data
atual = date.today().year ##data do ano atual
totmaior = 0
totmenor = 0
for c in range (1, 5):
    ano = int(input(f"Digite o ano de nascimento da {c}ª pessoa\n"))
    if atual - ano < 18:
        totmenor += 1
    else:
        totmaior += 1
print(f'''{totmenor} pessoas não atingiram a maioridade
{totmaior} pessoas atingiram a maioridade''')
