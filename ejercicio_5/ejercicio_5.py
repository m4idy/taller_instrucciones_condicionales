print(".................................................................")
print("...................Gasto de agua ................................")
print(".................................................................")


costo_fijo=1000

a="ingrese el valor del costo del agua"


if (str(a<50)):
    costo_agua=a

if (a<=200):
    costo_agua=a+2000+(a-50)

else: 
    costo_agua=a+3000+(a-50)
     
   