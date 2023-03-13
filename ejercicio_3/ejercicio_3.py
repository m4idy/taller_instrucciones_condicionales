print(".................................................................")
print(".........................PAPELERIA ..............................")
print(".................................................................")

# imput

a=int(input("ingrese el valor del precio_costo"))


if (a<3000):
   ganancia=0.15*a

if (a<=6000):
   ganancia=500
else:
   ganancia=0.25*a

precio_venta=ganancia + a

print(precio_venta)