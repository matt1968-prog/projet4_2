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
        joueur = Joueur(uuid4(), nom_joueur["nom"], prenom_joueur["prenom"], dob["dob"], sex["sexe"], id_nat["id_nat"], rating["rating"])
        self.database.joueurs.append(joueur)
        self.database.save(FILENAME)
