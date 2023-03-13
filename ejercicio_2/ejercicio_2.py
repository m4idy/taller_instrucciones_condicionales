print(".................................................................")
print("...................prestamo banco..........................")
print(".................................................................")

# imput

a=int(input("ingrese el valor de ingresos"))
b=int(input("ingrese el valor de deudas"))


if (a>945200):
    if (b==1):
        rta="NO APROBADO"
    else:
        rta="APROBADO"
else:
    rta="NO APROBADO"
print(rta)       