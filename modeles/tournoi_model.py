from typing import List
from ..modeles.player import Joueur
from UUID import UUID


class Tournoi:
    def __init__(self, id: UUID, nom_tournoi: str, lieu_tournoi: str, date_debut_tournoi, date_fin_tournoi, joueurs: List[Joueur], description: str, nombre_tours=4):
        self.id = id
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.date_debut_tournoi = date_debut_tournoi
        self.date_fin_tournoi = date_fin_tournoi
        self.joueurs = joueurs

    def add_joueur(self, joueur: Joueur):
        self.joueurs.append(joueur)

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "title": self.titre,
            "joueurs": [j.id for j in self.joueurs],
        }
