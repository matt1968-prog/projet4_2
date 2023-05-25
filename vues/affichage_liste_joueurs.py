from typing import List
from modeles.player import Joueur


class ShowPlayerListView:
    def __init__(self, joueurs: List[Joueur]):
        self.joueurs = joueurs

    def display(self):
        print("Liste des joueurs")
        print("=" * 20)
        print("Liste des joueurs par classement ELO")
        print()
        self.joueurs.sort(key=lambda j: j.rating, reverse=True)      
        #print(self.joueurs)
        
        """for i in self.joueurs:
            print("Nom : {i.nom} Pr�nom {i.prenom)}")"""
        
        for joueur in self.joueurs:
            print(f"- {joueur.nom} - {joueur.prenom} - {joueur.rating}")
        
        print()
        print("Liste des joueurs par classement alphabétique")
        print()
        self.joueurs.sort(key=lambda j: j.nom, reverse=False)
        for joueur in self.joueurs:
            print(f"- {joueur.nom} - {joueur.prenom}")