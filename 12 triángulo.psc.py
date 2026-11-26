import math

c1 = float(input("Introduce el primer cateto: "))
c2 = float(input("Introduce el segundo cateto: "))

h = math.sqrt(c1 * c1 + c2 * c2)

print("La hipotenusa del triangulo es:", h)