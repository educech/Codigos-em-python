print ("-=-"*20)
print("Analisador de triângulos")
print ("-=-"*20)
s1 = float(input("Primeiro segmento:\n"))
s2 = float(input("Segundo segmento:\n"))
s3 = float(input("terceiro segmento:\n"))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
    print("Essas medidas formam um triangulo")
else:
    print("Essas medidas não fomam um triangulo")