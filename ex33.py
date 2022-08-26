a = int(input("Digite o primeriro valor:\n"))
b = int(input("Digite o segundo valor:\n"))
c = int(input("Digite o terceiro valor:\n"))
m = a
if b<a and b<c:
    m = b
if c<a and c<b:
    m = c
print(f"O menor valor é {m}")##CALCULANDO O MENOR VALOR

ma = a
if b>a and b>c:
     ma = b
if c>a and c>b:
     ma = c
print(f"O maior valor é {ma}")## CALCULANDO O MAIOR VALOR



