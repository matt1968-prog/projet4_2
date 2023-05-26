from modeles.tour import Round
#from controleurs.creation_tours import 
from vues.round import CreationTourView
from uuid import UUID, uuid4
from datetime import datetime


class TourControleur:

    def __init__(self, id: UUID, round_name, round_number, date_heure_debut, python tournoi.py
    date_heure_fin, matchs):
        pass

    def create(self):
        vue = CreationTourView(id, round_name, round_number, date_heure_debut, date_heure_fin, [])
        data_round = []
        id, round_name, round_number, date_heure_debut, date_heure_fin, matchs = vue.creer_tour()
        round = Round(id, round_name, round_number, date_heure_debut, date_heure_fin, [])