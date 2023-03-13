from math import sqrt

print("-----------------------------------------------")
print("--------RESOLVER EC. DE SEGUNDO GRADO----------")
print("-----------------------------------------------")

# INPUT

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

# prossesing

d = sqrt((b*b)-4*a*c)

if d<0 :


  rta = "Es un valor imaginario"

if d == 0 :

    e = -b/a

    rta = "X1=X2, por lo tanto su unico valor será: " + str (e)

else :

    if d>0 :

        x = -b+d
        y = -b-d
        j = 2*a
        f = x/j
        g = y/j

        rta = "X1 = " + str (f) + " X2 = " + str (g)


print (rta)
