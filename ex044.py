'''p = float(input("Digite o preço do produto\n"))## PREÇO[
print("FORMAS DE PAGAMENTO\n")
print("DIGITE (1) PARA: À VISTA (DINHEIRO OU CHEQUE)")
print("DIGITE (2) PARA: À VISTA (NO CARTÂO)")
print("DIGITE (3) PARA: DIVIDIR 2x NO CARTÃO")
print("DIGITE (4) PARA: 3x OU MAIS NO CARTÃO\n")
condição = int(input("ESCOLHA A CONDIÇÃO DE PAGAMENTO\n"))
if condição == 1:
    print(f"O produto que custa {p}R$, sendo pago á vista (dinheiro ou cheque), terá 10% de desconto, CUSTARÁ : {p - (p * 10/100):.2f}R$")
elif condição == 2:
    print(f"O produto que custa {p}R$, sendo pago á vista (cartão), terá 5% de desconto, CUSTARÁ : {p - (p * 5/100):.2f}R$")
elif condição == 3:
    print(f"O produto que custa {p}R$, sendo pago em 2x (no cartão), terá o preço formal, CUSTARÁ : {p}R$")
else:
    pa = int(input("Quantas parcelas:\n"))##NUMERO DE PARCELAS
    print(f"O produto parcelado em {pa}X, custará {(p + p * 20/100)/pa :.2f}R$ a parcela")##p PREÇO DIVIDO POR  PARCELAS
    print(f"Sendo pago em {pa}x (no cartão), terá um juros 20%, CUSTARÁ : {p + (p * 20/100):.2f}R$")'''


print("EDUARDO CONFECÇÕES\n")
compra = float(input("Digite o valor da compra:\n"))
print("FORMAS DE PAGAMENTO")
print('''[1] Á VISTA NO DINHEIRO
[2] Á VISTA NO CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO\n''')
forma = int(input("Escolha  a forma de pagamento:\n"))
if forma == 1:
    total = compra - (compra * 10/100)
elif forma == 2:
       total = compra - (compra * 5/100)
elif forma == 3:
    total = compra
    valpar = compra/2
    print(f"O valor da compra será dividido em 2x de {valpar:.2f} SEM JUROS ")
elif forma == 4:
    parcela = int(input("Digite a quantidade de parcelas\n"))
    total = compra + (compra * 20/100)
    valpar = total/parcela
    print (f"O valor da compra sera dividido em {parcela} parcelas de {valpar:.2f} com 20% DE JUROS")
else:
    total = 0
    print("OPÇÃO INVÁLIDA DE PAGAMENTO")
print(f"O valor de {compra:.2f} custará {total:.2f} no final")##ESSE PRINT VALERÁ PARA TODOS OS OUTROS PRINTS

