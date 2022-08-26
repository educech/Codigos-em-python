''''a = float(input("Digite o primeiro segmento:\n"))
b = float(input("Digite o segundo segmento:\n"))
c = float(input("Digite o terçeiro segmento:\n"))
if a > b + c or b > c + a or  c > a + b:
    print("Os segmentos acima NÃO PODEM FORMAR um TRIÂNGULO")#QUANDO UM SEGMENTO É MAIOR QUE A SOMA DOS OUTROS DOIS
elif a == b and b == c and c == a:
    print("Os segmentos acima PODEM FORMAR um TRIÂNGULO EQUILÁTERO")#TODOS OS LADOS IGUAIS
elif a == b and  c != a and c != b or a==c and b!= a and b != c or c == b and a!= b and a != c:
    print("Os segmentos acima PODEM FORMAR um TRIÂNGULO ISÓSCELES")# 2 LADOS IGUAIS E UM LADO DIFERENTE
elif a != b and b != c and c != a:
    print("Os segmentos acima PODEM FORMAR um TRIÂNGULO ESCALENO")# TODOS OS LADOS DIFERENTE'''

##FORMA DIFERENTE DE ANINHAR

a = float(input("Digite o primeiro segmento:\n"))
b = float(input("Digite o segundo segmento:\n"))
c = float(input("Digite o terçeiro segmento:\n"))
if a < b + c and b < c + a and  c < a + b:
    print("Os segmentos acima PODEM FORMAR um TRIÂNGULO", end=' ')
    if a == b == c :
        print("EQUILÁTERO")
    elif a != b != c != a != b: #DIFERENTE TEM QUE DAR UMA ATENÇÃO MAIOR
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um TRIÂNGULO")