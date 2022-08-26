peso = float(input("Digite seu peso:\n"))
altura = float(input("Digite sua altura:\n"))
imc = peso/(altura ** 2)
print(f"Seu IMC é de : {imc:.1f}")
if imc < 18.5:
    print("CUIDADO!!! Você está ABAIXO DO PESO normal")
elif 18.5 <= imc < 25:
    print("Parabéns vocÇe esta com o PESO IDEAL!!")
elif 25 <= imc < 30:
    print("Você esta com SOBREPESO")
elif 30 <= imc <= 40:
    print("Você esta OBESO")
else:
    print("CUIDADO!!! você está com OBESIDADE MÓRBIDA")

