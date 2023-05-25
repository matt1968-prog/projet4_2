from modeles.database_model import Database


FILENAME = "data.json"


class BaseController:
    def __init__(self, database: Database):
        self.database = database


"""class MainController(BaseController):
    def execute(self):
        while True:
            view = MainView()
            choix = view.display()
            controller = None
            if choix == 1:
                controller = AddPlayerController(self.database)
            elif choix == 2:
                controller = ShowPlayerListController(self.database)
            elif choix == 3:
                return

            if controller:
                controller.execute()"""
