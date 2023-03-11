
print("......................................................")
print("..................TRIANGULOS..........................")
print("......................................................")

# INPUT

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))


# output 

if  a==b==c : 
    rta= "es un triangulo agudo"

if  a==b or b==a or b==c or c==b or c==a or a==c :
     rta= "es un trianulo recto"
else: 
     rta= "es un triangulo obstuso" 

print (rta)