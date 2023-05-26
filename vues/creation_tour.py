#import json
from uuid import UUID, uuid4
from typing import List


class CreationTourView:
    def __init__(self, id: UUID, round_name: str, round_number: int,
                 date_heure_debut: str, date_heure_fin: str, matchs: List):
        self.id = id
        self.round_name = round_name
        self.round_number = round_number
        self.date_heure_debut = date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.matchs = matchs

    def creer_tour(self):
        id = uuid4()
        round_name = self.round_name
        round_number = self.round_number
        date_heure_debut = self.date_heure_debut
        date_heure_fin = self.date_heure_fin
        matchs= []

        return id, round_name, round_number, date_heure_debut, date_heure_fin, matchs
    #def display_round():
        #pass
