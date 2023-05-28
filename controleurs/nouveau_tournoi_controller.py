from controleurs.base_controller import BaseController
from modeles.tournoi import Tournoi
from vues.affichage_tournoi_view import DisplayTournamentView
from uuid import UUID, uuid4
from pprint import pprint
from datetime import datetime
import locale
FILENAME = "data.json"


class AddNewTournament (BaseController):
    
    def execute(self):
        view = DisplayTournamentView()
        data_tournoi = view.display()
        # view = AddPlayerView()
        # view = DisplayTournamentView(tournoi)
        #data_tournoi = view.display()
        tournoi = Tournoi(uuid4(), data_tournoi["nom_tournoi"], data_tournoi["lieu_tournoi"], data_tournoi["date_debut_tournoi"], data_tournoi["date_fin_tournoi"], data_tournoii["type_tournoi"], data_tournoi["description"], data_tournoi["nombre_tours"])
        self.database.tournois.append(tournoi)
        self.database.save(FILENAME)


class CreationTournoiView:
    def __init__(self):
        pass

    def creer_tournoi(self):
        libelle_tournoi = {'1': 'Rapide', '2': 'Blitz', '3': 'Bullet'}
        #id=uuid4()
        nom_tournoi = input("Nom du tournoi :\n")
        lieu_tournoi = input("Lieu du tournoi :\n")
        locale.setlocale(locale.LC_ALL, "fr-FR.UTF8")
        while True:
            try:
                date_debut = input("Date de dÃ©but du tournoi (au format JJ mois AAAA) : ")
                date_debut_tournoi = datetime.strptime(date_debut, "%d %B %Y")
                date_debut_tournoi = date_debut_tournoi.strftime("%d %b %Y")
                break
            except (ValueError, TypeError):
                print("Format de date incorrect. Le format doit Ãªtre de type jj mois YYYY (ex : 20 juin 2023) avec un espace entre chaque.")

        while True:
            try:
                date_fin = input("Date de fin du tournoi (au format JJ mois AAAA) : ")
                date_fin_tournoi = datetime.strptime(date_fin, "%d %B %Y")
                date_fin_tournoi = date_fin_tournoi.strftime("%d %b %Y")
                print(f"Date de fin du tournoi : {date_fin_tournoi}")
                break
            except (ValueError, TypeError):
                print("Format de date incorrect. Le format doit Ãªtre de type jj mois YYYY (ex : 21 juin 2023) avec un espace entre chaque.")

        while True:
            try:
                type_tournoi = int(input("Type de tournoi : Rapide(1), Blitz(2), Bullet(3) (Rapide par d�faut) : \n"))
                if type_tournoi > 0 and type_tournoi < 4:
                    break
            except ValueError:
                print("La valeur doit �tre un nombre entier compris entre 1 et 3")

        description = input("Description facultative du directeur du tournoi\n")
        nombre_tours = 4
        libelle_type_tournoi = libelle_tournoi.get(str(type_tournoi))
        print(f"Type de tournoi : {libelle_type_tournoi}")
        # nouveau_tournoi = Tournoi(self.nom_tournoi, self.lieu_tournoi,
        # self.date_debut_tournoi, self.date_fin_tournoi, self.type_tournoi, self.description, self.nombre_tours)

    def afficher_tournoi(self):
        TOURNAMENT_TYPE = {1: "Rapide", 2: "Blitz", 3: "Bullet"}
        print()
        print(f"R�capitulatif du nouveau tournoi {nom_tournoi} : ")
        print()
        print(f"Nom du tournoi : {nom_tournoi}")
        print(f"Lieu : {lieu_tournoi}")
        print(f"Date de d�but : {date_debut_tournoi}")
        print(f"Date de fin : {date_fin_tournoi}")
        type_tournoi = int(type_tournoi)
        print(f"Type de tournoi : {TOURNAMENT_TYPE[type_tournoi]}")  # ({self.type_tournoi}) ")
        print(f"Description du directeur du tournoi : {description}")

        return nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, type_tournoi, description, nombre_tours
