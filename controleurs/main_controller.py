from controleurs.base_controller import BaseController
from vues.main_view import MainView
from controleurs.player_list_controller import ShowPlayerListController
from controleurs.nouveau_tournoi_controller import AddNewTournament
from controleurs.controleur_joueur import AddPlayerController
from vues.ajout_tournoi import CreationTournoiView


class MainController(BaseController):
    def execute(self):
        while True:
            view = MainView()
            choix = view.display()
            controller = None
            if choix == 1:
                controller = AddNewTournament()
            if choix == 2:
                pass
            if choix == 3:
                pass
            elif choix == 4:
                controller = AddPlayerController(self.database)
            if choix == 5:
                controller = ShowPlayerListController(self.database)
            if choix == 6:
                pass
            if choix == 7:
                pass
            elif choix == 0:
                return

            if controller:
                controller.execute()
