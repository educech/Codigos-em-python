f = str(input("Digite uma frase:\n")).strip().upper()
print(f"A letra A aparece {f.count('A')} vezes")
print(f"Ela aparece a primeira vez na posição {f.find('A')}")
print(f"Ela aparece a última vez na posição {f.rfind('A')} ")