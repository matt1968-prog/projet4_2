from controleurs.base_controller import BaseController
from modeles.tournoi import Tournoi
from vues.affichage_tournoi_view import DisplayTournamentView
from uuid import UUID, uuid4
from pprint import pprint
from datetime import datetime
import locale
FILENAME = "data.json"


class AddNewTournament ():
    
    def __init__(self, database):
        self.database = database

    def execute(self):
        view = DisplayTournamentView()
        data_tournoi = view.display()
        # view = AddPlayerView()
        # view = DisplayTournamentView(tournoi)
        #data_tournoi = view.display()
        tournoi = Tournoi(uuid4(), data_tournoi["nom_tournoi"], data_tournoi["lieu_tournoi"], data_tournoi["date_debut_tournoi"], data_tournoi["date_fin_tournoi"], data_tournoii["type_tournoi"], data_tournoi["description"], data_tournoi["nombre_tours"])
        self.database.tournois.append(tournoi)
        self.database.save(FILENAME)

