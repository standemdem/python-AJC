dico= {
    'mineur' : list(range(0,18)),
    'majeur' : list(range(19, 51)),
    'senior' : list(range(50, 101)),
    'mort': list(range(100, 200))
}

age = int(input("Entre ton age"))
for item in dico.items():
    if age in item[1]:
        print(f"tu es {item[0]}")