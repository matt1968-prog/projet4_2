from typing import List
from modeles.player import Joueur
from modeles.tournoi import Tournoi


class DisplayTournamentView:
    """def __init__(self, tournois: List[Tournoi]): 
        self.tournois = tournois
    """

    def __init__(self, tournoi: List[Tournoi]):
        self.tournoi = tournoi
    
    def display(self):
        print("Tournoi en cours : \n")
        print("=" * 20)

        for tourney in self.tournoi:
            print(f"- {tourney.nom_tournoi} {tourney.lieu_tournoi}")
