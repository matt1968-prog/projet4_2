from vues.affichage_liste_joueurs import ShowPlayerListView
from vues.ajout_joueur import AddPlayerView
from controleurs.base_controller import BaseController
from modeles.player import Joueur
from uuid import uuid4
FILENAME = "data.json"


class AddPlayerController(BaseController):
    def execute(self):
        view = AddPlayerView()
        data_player = view.display()
        joueur = Joueur(uuid4(), data_player["nom"], data_player["prenom"], data_player["dob"], data_player["sex"], data_player["id_nat"], data_player["rating"])
        self.database.joueurs.append(joueur)
        self.database.save(FILENAME)
