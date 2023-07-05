menu={
    '1': 'Orange',
    '2': 'Banane',
    '3': 'pizza hawaienne démoniaque'
}
a = [print(f"{i[0]} : {i[1]}") for i in menu.items()]
input = input("entre le chiffre correspondant à votre choix: ")
print(f"Vous avez choisi le menu {input} : {menu[input]}" )