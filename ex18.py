'''import math
n = float(input(" Digite um angulo: "))
seno = math.sin(math.radians(n))
print (f"O angulo de {n} tem o seno de {seno:.2f}")
cos = math.cos(math.radians(n))
print(f"O ângulo de {n} tem o cosseno de {cos:.2f}")
tan = math.tan(math.radians(n))
print(f"O ângulo de {n} tem a tangente de {tan:.2f}")'''

from math import sin, cos, tan, radians
n = float(input(" Digite um angulo: "))
###seno = sin(radians(n))
print (f"O angulo de {n} tem o seno de {sin(radians(n)):.2f}")
###cos = cos(radians(n))
print(f"O ângulo de {n} tem o cosseno de {cos(radians(n)):.2f}")
###tan = tan(radians(n))
print(f"O ângulo de {n} tem a tangente de {tan(radians(n)):.2f}")





