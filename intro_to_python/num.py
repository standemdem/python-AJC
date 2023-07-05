def arithmetique(a, b):
    print("opération arithmétiques : ")
    print(a +b)
    print(a / b)
    print(a * b)
    print(a - b)

def unaires(a):
    double =a
    double *=2
    triple = a
    triple*=3
    moitie =a
    moitie /=2
    print(a, double, triple, moitie )

def complexee(a, b):
    comp=complex(a,b)
    print(comp)

arithmetique(3, 5)
unaires(4)
complexee(3, 4)