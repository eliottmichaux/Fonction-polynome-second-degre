from math import*

def polynome_second_degre():
    a = float (input ("Rentrer le réel a"))
    b = float (input ("Rentrer le réel b"))
    c = float (input ("Rentrer le réel c"))
    delta = b**2 - 4*a*c
    if delta < 0 :
        print ("Delta est négatif, il n'a donc pas de racine")
    if delta > 0 :
        x1 = (-b -sqrt(delta)) / 2*a
        x2 = (-b + sqrt(deltaa))/2*a
        print ("Delta est positif, il existe deux solutions \n" + "x_1 = "+str(x_1)+" \n"+"x_2 = "+str(x_2))
    elif delta == 0 :
        x_0 = -b/2*a
        print ("Delta est nul, il n'a donc qu'une seule racine qui est \nx_0 = "+str (x_0))

str (polynome_second_degre())
