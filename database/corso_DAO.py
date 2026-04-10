# Add whatever it is needed to interface with the DB Table corso


from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


class CorsoDAO:

    @staticmethod
    def get_all() -> list[Corso]:
        cnx = get_connection()
        if cnx is None:
            return []

        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT codins, crediti, nome, pd FROM corso ORDER BY nome")

            res = []
            for row in cursor.fetchall():
                res.append(
                    Corso(
                        codins= row["codins"],
                        crediti= row["crediti"],
                        nome= row["nome"],
                        pd= row["pd"]
                    )
                )
            cursor.close()
            return res

        finally:
            cnx.close()


    @staticmethod
    def get_iscritti(codins: str) -> list[Studente]:
        cnx = get_connection()
        if cnx is None:
            return []

        try:
            cursor = cnx.cursor(dictionary=True)
            query = """
                            SELECT s.matricola, s.cognome, s.nome, s.CDS
                            FROM studente s
                            JOIN iscrizione i ON s.matricola = i.matricola
                            WHERE i.codins = %s
                            ORDER BY s.cognome, s.nome
                        """
            cursor.execute(query, (codins,))
            res = []
            for row in cursor.fetchall():
                res.append(
                    Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
                )
                cursor.close()
                return res

        finally:
            cnx.close()

    @staticmethod
    def get_corsi_by_student(matricola: int) -> list[Corso]:
        cnx = get_connection()
        if cnx is None:
            return []

        try:
            cursor = cnx.cursor(dictionary=True)
            query = """
                            SELECT c.codins, c.crediti, c.nome, c.pd
                            FROM corso c
                            JOIN iscrizione i ON c.codins = i.codins
                            WHERE i.matricola = %s
                            ORDER BY c.nome
                        """
            cursor.execute(query, (matricola,))
            res = []
            rows = cursor.fetchall()
            for row in rows:
                res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
            cursor.close()
            return res

        finally:
            cnx.close()

    @staticmethod
    def iscrivi(matricola: int, codins: str) -> bool:
        cnx = get_connection()
        if cnx is None:
            return False

        try:
            cursor = cnx.cursor()
            cursor.execute("INSERT INTO iscrizione(matricola, codins) VALUES (%s, %s)",
                (matricola, codins)
            )
            cnx.commit()
            cursor.close()
            return True

        except Exception:
            cnx.rollback()
            return False
        finally:
            cnx.close()