print("="*30)
print(" "*8,"10 TERMOS"," "*8)
print("="*30)
primeiro = int(input("Digite o 1º termo da P.A:\n"))
razao = int(input("Digite a razão:\n"))
decimo = primeiro + (10 - 1)* razao ## FORMULA PARA EMCONTRAR O DECIMO TERMO, OU QUALQUER OUTRO QUE EU QUEIRA.
for c in range (primeiro, decimo + razao, razao):
    print(f'{c}',end=" -> ")
print("ACABOU")