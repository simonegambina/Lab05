from database.corso_DAO import CorsoDAO

corsi = CorsoDAO.get_all()
print(len(corsi))
print(corsi[0])