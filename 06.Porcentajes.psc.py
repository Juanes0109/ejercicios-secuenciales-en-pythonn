cd = float(input("Ingrese la cantidad de dinero invertido: "))
pd = float(input("Ingrese el porcentaje de intereses: "))
pin = float(input("Ingrese el periodo de tiempo en días: "))

vin = (cd * pd / 100 * pin) / 360
vim = vin * 0.07
vt = cd + vin - vim

print("El valor de intereses es", vin)
print("El valor de impuestos es", vim)
print("El valor total a pagar es", vt)