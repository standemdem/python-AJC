from errors import GenderError,MaxAgeERoor,MinAgeError, Errors
from foot_team import Player, Team

def start_menu():
    print("Welcome to Team Manager ")
    print("------------------------")
    print("1) Create a player ")
    print(" Press any other key to quit Class Manager")
    return int(input())

if __name__=="__main__":
    team = Team()

    while True:
        choice = start_menu()
        if choice == 1:
            try:
                nom = input("Nom du joueur : ")
                age = int(input("Âge du joueur : "))
                sexe = input("Sexe du joueur (F/f) : ")
                numero = input("Numéro du joueur : ")

                joueur = Player(nom, age, sexe, numero)

                if joueur.age < 18:
                    raise MinAgeError("L'âge du joueur est inférieur à 18 ans.")
                elif joueur.age > 35:
                    raise MaxAgeERoor("L'âge du joueur est supérieur à 35 ans.")
                elif joueur.sexe.upper() not in ['F']:
                    raise GenderError("Le sexe du joueur est différent de 'F' ou 'f'.")

                print("Joueur enregistré avec succès !")

            except ValueError:
                print("Erreur : l'âge du joueur doit être un nombre entier.")
            except Errors as e:
                print("Erreur :", str(e))
        else:
            break
    # play1 = Player("bob", 12, "F", "7")
    # team_rocket = Team()
    # team_rocket.add_to_team(play1.get_player())
    # [print(player) for player in team_rocket.list_of_players]