sb = float(input("Ingrese el valor de su salario base: "))

s = (sb * 4) / 100
p = (sb * 4) / 100
td = s + p
sn = sb - td

print("El valor del aporte en salud es", s)
print("El valor del aporte en pension es", p)
print("El total de descuento por estos aportes es", td)
print("El salario neto despues del descuento de los aportes es", sn)