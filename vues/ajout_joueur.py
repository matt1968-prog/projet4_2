from typing import List
from modeles.player import Joueur


class MainView:
    def display(self) -> int:
        print()
        print("1 - Ajouter joueur")
        print("2 - Afficher listes des joueurs")
        print("3 - Quitter le programme")
        while True:
            try:
                choix = int(input("Choix: "))
            except ValueError:
                pass
            else:
                return choix


class AddPlayerView:
    def display(self) -> dict:
        print("Ajout d'un nouveau joueur\n")
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        dob = input("Date de naissance : ")
        sexe = input("Sexe : ")
        id_nat = input("ID National : ")
        rating = int(input("Classement ELO : "))
        return {"nom": nom, "prenom": prenom, "dob": dob, "sexe": sexe, "id_nat": id_nat, "rating": rating}


class ShowPlayerListView:
    def __init__(self, joueurs: List[Joueur]):
        self.joueurs = joueurs

    def display(self):
        print("Liste des joueurs")
        print("=" * 20)

        for joueur in self.joueurs:
            print(f"- {joueur.nom} - {joueur.prenom}")