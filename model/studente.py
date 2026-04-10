class Studente:
    def __init__(self, matricola: int, nome: str, cognome: str, cds: str | None = None):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.cds = cds

    def __str__(self):
        return f"{self.cognome} {self.nome} ({self.matricola})"
