from modeles.player import Joueur
from typing import List
from uuid import UUID


class Tournoi:
    def __init__(self, id: UUID, titre: str, joueurs: List[Joueur]):
        self.id = id
        self.titre = titre
        self.joueurs = joueurs

    def add_joueur(self, joueur: Joueur):
        self.joueurs.append(joueur)

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "title": self.titre,
            "joueurs": [j.id for j in self.joueurs],
        }