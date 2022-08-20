
chave = input("Digite a base da sua senha: ")
senha = " "

for letra in chave:
    if letra in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "12"
    elif letra in "Cc": senha = senha + "13"
    elif letra in "Dd": senha = senha + "14"
    elif letra in "Ee": senha = senha + "15"
    elif letra in "Ff": senha = senha + "16"
    elif letra in "Gg": senha = senha + "&"
    elif letra in "Ss": senha = senha + "*"
    elif letra in "Tt": senha = senha + "%"
    elif letra in "Ll": senha = senha + "#"
    else: senha = senha + letra


print(senha)


