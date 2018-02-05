#coding: utf-8
x=input("Indique un num:")
y=input("Indique un num mayor que "+str(x)+": ")
while x>=y:
    y=input(str(y)+" no es mayor "+str(x)+" intentelo otra vez: ")
z=float(input("Indique un num entre "+ str(x)+" y "+str(y)+": "))
count=0
while x<=z<=y:
    count+=1
    z=float(input("Indique un num entre "+str(x)+" y "+str(y)+": "))
if count==0:
    print "No ha introducido ningun num entre", x, "y", str(z) + "."
elif count==1:
    print "Has introducido 1 número entre", x, "y", str(z)+"."
else:
    print "Has introducido", count, "num entre", x, "y", str(y) + "."
print "Programa terminado"



