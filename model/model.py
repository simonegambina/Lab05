from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO


class Model:
    def __init__(self):
        self._corsi = []

    def load_corsi(self):
        self._corsi = CorsoDAO.get_all()
        return self._corsi

    def get_corsi(self):
        return self._corsi

    def get_iscritti_corso(self, codins: str):
        return CorsoDAO.get_iscritti(codins)

    def get_studente(self, matricola: int):
        return StudenteDAO.get_by_matricola(matricola)

    def get_corsi_studente(self, matricola: int):
        return CorsoDAO.get_corsi_by_student(matricola)

    def iscrivi(self, matricola: int, codins: str) -> bool:
        return CorsoDAO.iscrivi(matricola, codins)