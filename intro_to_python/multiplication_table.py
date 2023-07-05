num = int(input("entre un nombre entier: "))
table=[num * i for i in range(1,11)]
print(*table, sep=", ", end="")