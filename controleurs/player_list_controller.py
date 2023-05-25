from controleurs.base_controller import BaseController
from vues.affichage_liste_joueurs import ShowPlayerListView

class ShowPlayerListController(BaseController):
    def execute(self):
        view = ShowPlayerListView(self.database.joueurs)
        view.display()