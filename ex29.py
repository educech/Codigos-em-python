v = float(input("Qual a velocidade atual do carro:\n"))
m = (v-80)*7 #multa
if v <= 80:
    print("Bom dia!!, Dirija com seguraça.")
else:
    print("MULTADO!!!, Voçê excedeu o limite permitido que é de 80Km/h\n"
          f"Terá que pagar a multa de {m:.2f}R$!!\n"
          "Tenha um bom dia, dirija com segurança!!")