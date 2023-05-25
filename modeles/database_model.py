from typing import List, Optional
from modeles.player import Joueur
from modeles.tournoi import Tournoi
from uuid import UUID, uuid4
import json
import os


class Database:
    # def __init__(self, joueurs: List[Joueur], tournois: List[Tournoi]): ligne d'origine
    def __init__(self, joueurs: List[Joueur], tournois: List[Tournoi]):
        self.joueurs = joueurs
        self.tournois = tournois

    def get_joueur_by_id(self, id: UUID) -> Optional[Joueur]:
        for j in self.joueurs:
            if j.id == id:
                return j

        return None

    """def to_dict(self) -> dict:  fonction d'origine avec tournois
        return {
            "joueurs": [j.to_dict() for j in self.joueurs],
            "tournois": [t.to_dict() for t in self.tournois],
        }"""
    def to_dict(self) -> dict:
        return {
            "joueurs": [j.to_dict() for j in self.joueurs],
            "tournois": [j.to_dict() for j in self.tournois]
        }

    def save(self, FILENAME: str):
        with open(FILENAME, "w") as file:
            file.write(json.dumps(self.to_dict(), indent=4))

    @classmethod
    def load(cls, FILENAME: str) -> "Database":
        # pass
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as file:
                data = json.loads(file.read())
                joueurs = [Joueur(**data_joueur) for data_joueur in data["joueurs"]]
                tournois = []
                for data_tournoi in data["tournois"]:
                    tournoi = Tournoi(data_tournoi["id"], data_tournoi["title"], [])
                    # ajout des joueurs dans l'instance tournois
                    for joueur_id in data_tournoi["joueurs"]:
                        selected_joueur = [j for j in joueurs if j.id == joueur_id]
                        if len(selected_joueur) > 0:
                            tournoi.add_joueur(selected_joueur[0])
                    # --
                    tournois.append(tournoi)

                return Database(joueurs, tournois)
        else:
            # database = Database([], []) ligne origine avec tournoi
            database = Database([], [])
            database.save(FILENAME)
            return database
