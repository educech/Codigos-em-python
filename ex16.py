'''import math
n = float(input("Digite um numero "))
print (f"O valor digitado foi {n}, e sua porção inteira é {math.trunc(n)}")'''

'''from math import trunc
n = float(input("Digite um numero "))
print (f"O valor digitado foi {n}, e sua porção inteira é {trunc(n)}")'''


print("#-#-" * 20)
print("\033[4;30;42;m PORÇÃO INTEIRA \033[m")
print("#-#-" * 20)
n = float(input("\033[0;30;44;m Digite um número \033[m\n"))
print (f"O valor digitado foi {n}, e sua porção inteira é {int(n)}")


