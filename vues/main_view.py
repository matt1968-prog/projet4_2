class MainView:
    def display(self) -> int:
        print()
        choix = -1
        print("1 - Créer Nouveau tournoi")
        print("2 - Charger tournoi existant")
        print("3 - Affichage des données du tournoi actuel")
        print("4 - Ajouter joueur")
        print("5 - Afficher listes des joueurs")
        print("6 - Création des matchs du tour à venir et affichage des matchs")
        print("7 - Saisie des resultats du tour terminé")
        print("8 - Classement du tournoi")
        print("0 - Quitter le programme")

        while choix != 0:
            try:
                choix = int(input("Choix: "))
            except ValueError:
                print(f"Valeur {choix} non valide. Faites un autre choix.")
            if choix < 0 or choix > 8:
                print("La valeur doit être un entier compris entre 0 et 8\n")
            else:
                return choix