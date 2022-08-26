n = int(input("Digite um numero inteiro:\n"))
b = int(input("""ESCOLHA UMA DAS BASES PARA CONVERSÂO:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL\n"""))
print(f"Sua opção: {b}")

if b == 1:
    print(f"O NUMERO {n} em BINÁRIO é {bin(n)[2:]}")
elif b == 2:
    print(f"O numero {n} em OCTAL é {oct(n)[2:]}")
elif b == 3:
    print(f"O numero {n} em HEXADECIMAL é {hex(n)[2:]}")
else:
    print("OPÇÃO INVALIDA, TENTE NOVAMENTE.")
