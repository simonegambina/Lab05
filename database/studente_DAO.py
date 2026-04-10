# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class StudenteDAO:

    @staticmethod
    def get_by_matricola(matricola: int) -> Studente | None:
        cnx = get_connection()
        if cnx is None:
            return None

        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(
                "SELECT matricola, cognome, nome, CDS FROM studente WHERE matricola = %s",
                (matricola,)
            )
            row = cursor.fetchone()
            cursor.close()

            if row is None:
                return None

            return Studente(
                matricola=row["matricola"],
                cognome=row["cognome"],
                nome=row["nome"],
                cds=row["CDS"]
            )
        
        finally:
            cnx.close()