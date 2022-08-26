soma = 0 ##VAI SOMAR TODOS OS NÚMEROS
cont = 0 ##VAI CONTAR QUANTOS NÚMEROS
for c in range (1, 7): ## CONTARA OS NUMEROS DE 1 A 6
    n = int(input(f"Digite o {c}º valor:\n"))##DENTRO DO RANGE ESSE COMANDO EXECUTARÁ 6 VEZES
    if n % 2 == 0: ## SÓ SOMARÁ E CONTARÁ OS NÚMEROS QUE FOREM PARES
        soma = soma + n
        cont = cont + 1
print(f"Você informou {cont} números PARES, e a soma de todos el é {soma}")