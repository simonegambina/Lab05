class Corso:
    def __init__(self, codins: str, crediti: int, nome: str, pd: int):
        self.codins = codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd

    def __str__(self):
        return f"{self.nome} ({self.codins})"
