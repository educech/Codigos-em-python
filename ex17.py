'''co = float(input("Qual o valor do cateto oposto: "))
ca = float(input("Qual o valor do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print (f"a soma dos catetos é igual a {co ** 2 + ca ** 2}, e o valor da hipotenusa é {hi}")'''

'''import math
co = float(input("Qual o valor do cateto oposto: "))
ca = float(input("Qual o valor do cateto adjacente: "))
hi = math.hypot(co, ca)
print (f"O valor da hipotenusa é {hi}")'''

from math import hypot
co = float(input("Qual o valor do cateto oposto: "))
ca = float(input("Qual o valor do cateto adjacente: "))
hi = hypot(co, ca)
print (f"O valor da hipotenusa é {hi:.2f}")


