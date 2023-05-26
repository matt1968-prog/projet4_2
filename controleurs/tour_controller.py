from ..controleurs.base_controller import BaseController


class CreateRoundController():

    def __init__(self):
        pass

    def create(self):
        vue = CreationTourView(id, round_name, round_number, date_heure_debut, date_heure_fin, [])
        data_round = []
        id, round_name, round_number, date_heure_debut, date_heure_fin, matchs = vue.creer_tour()
        round = Round(id, round_name, round_number, date_heure_debut, date_heure_fin, [])  = 


    "def __init__(self, id: UUID, round_name, round_number, date_heure_debut, python tournoi.py

    """def create(self):
        vue = CreationTourView(id, round_name, round_number, date_heure_debut, date_heure_fin, [])
        data_round = []
        id, round_name, round_number, date_heure_debut, date_heure_fin, matchs = vue.creer_tour()
        round = Round(id, round_name, round_number, date_heure_debut, date_heure_fin, [])""""
    
    """def __init__(self, id: UUID, round_name, round_number, date_heure_debut,
                 date_heure_fin, matchs):
        pass

    def create(self):
        vue = CreationTourView(id, round_name, round_number, date_heure_debut, date_heure_fin, [])
        data_round = []
        id, round_name, round_number, date_heure_debut, date_heure_fin, matchs = vue.creer_tour()
        round = Round(id, round_name, round_number, date_heure_debut, date_heure_fin, [])"""

