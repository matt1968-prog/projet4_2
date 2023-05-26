import json
import sys
from uuid import UUID, uuid4


class Joueur:
    def __init__(self, id: UUID, nom: str, prenom: str, dob, sexe, id_nat: str, rating, score=0):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.dob = dob
        self.id_nat = id_nat
        self.rating = rating
        self.sexe = sexe
        self.score = score

    def to_dict(self):
        return {"id": str(self.id), "nom": self.nom, "prenom": self.prenom, "dob": self.dob, "rating": self.rating, "sexe": self.sexe, "id_nat": self.id_nat, "score": self.score}

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"<Joueur id:{self.id} prenom:{self.prenom} nom: {self.nom}>"

"""class Joueur:
    def __init__(self, id: UUID, prenom: str, nom: str):
        self.id = id
        self.prenom = prenom
        self.nom = nom

    def to_dict(self) -> dict:
        return {"id": str(self.id), "prenom": self.prenom, "nom": self.nom}"""

