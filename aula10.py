##FATIAMENTO##

'''frase = "CURSO EM VIDEO PYTHON"
print(frase[5:13])''' #aqui fatio a str numerando as letras que quero que apareçam

'''print(
        Nessa aula, vamos aprender operações com String no Python.
        As principais operações que vamos aprender são o Fatiamento 
        de String, Análise com len(), count(), find(), 
        transformações com replace(), upper(), lower(), 
        capitalize(), title(), strip(), junção com join().)''' #dessa forma dou um print só para aparecer todo o texto



 ##COUNT##
'''frase = "curso em video python"
print(frase.count('o'))'''  #essa função conta quantos dos mesmos caracteres aparecem na frase

##UPPER##
'''frase = "curso em video python"
print(frase.upper().count('P'))''' #essa função coloca toda a frase em maiuscula

##LEN##
'''essa função mostra o numero de elementos contando os espaços'''

##STRIP##
'''frase = "    curso em video python   "
print(len(frase.strip()))''' ##essa função mostra o numero de elementos sem contar os espaços

##REPLACE##
'''frase = "curso em video python"
print(frase.replace('python', 'android'))''' ##essa função troca uma str da frase por outra sem precisar mudar a variaável frase


##lower##
'''frase = "Curso em Video Python"
print(frase.lower().count('P'))''' ##esa função transforma toda frase em minuscula

##FIND##
'''frase = "curso em video python"
print(frase.find('deo')''' ##essa função mostra onde começa tal sequencia de textos na str

##SPLIT##
'''frase = "curso em video python"
print(frase.split())'''##essa função cria lista para cada palavra [listas]

'''frase = "curso em video python"
dividido = (frase.split())
print(dividido[0][3]) ##aqui eu mostro uma str específca de uma lista criada'''

##CAPITALIZE
'''frase = "curso em video python"
print(frase.capitalize())'''

n1 = float(input("Digite a primeiera nota\n"))
n2 = float(input("Digite a segunda nota\n"))
m = (n1 + n2)/2
print(f"Sua media é {m}")
print('PARABENS!!' if m >= 6 else 'ESTUDE MAIS!!')
