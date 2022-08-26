
n = int(input("\033[1;32;m Digite um numero qualquer:\033[m\n"))
r = (n % 2)
if r==0: ##USO O MODULO % QUE DARÁ O RESTO DA DIVISÃO
    print(f"O nùmero {n} é par")
else:
    print((f"O número {n} é impar"))
