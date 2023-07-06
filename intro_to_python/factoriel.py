def factoriel(n):
    if n==1:
        return n
    return n * factoriel(n-1)

n= int(input("Entre un entier: \n"))
if n < 0 :
    print("fils de chlag, tu me prends pour un idiot ?")
else:
    print(factoriel(n))