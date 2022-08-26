from datetime import date
a = int(input("Digite o ano de seu nascimento:\n"))##ano que nasceu
b = date.today().year##ano atual
i = b - a ##idade atual
f = 18 - i ##qtd de anos que falta para se alistar
if a > b:
    print("INFORME UM ANO VÁLIDO")## caso coloque um ano maior do que o atual
elif a < 1900:
    print("Digite um ano de 1900 para cima")## caso coloque um ano abaixo de 1900
elif i < 18:
    print(f"""Quem nasceu em {a} tem {i} anos em {b}
ainda falta(m) {f} ano(s) para vc se alistar
seu alistamento será em {b + f}""")
elif i > 18:
    s = i - 18
    print(f"Você tem {i} anos em {b} voçê deveria ter se alistado ha {s}")
else:
    print(f"Voçê tem {i} anos em {b}, já pode se alistar")
