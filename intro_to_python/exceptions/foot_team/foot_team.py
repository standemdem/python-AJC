from errors import GenderError, MaxAgeERoor, MinAgeError
class Player:

    def __init__(self, name, age, sexe, number):
            self.name = name
            self.age = age
            self.sexe = sexe
            self.number= number

    def get_player(self):
        return self.name

class Team:

    def __init__(self) -> None:
        self.list_of_players = []

    def add_to_team(self, player):
        return self.list_of_players.append(player)