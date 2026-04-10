from database.studente_DAO import StudenteDAO

s = StudenteDAO.get_by_matricola(146101)
print(s)

s2 = StudenteDAO.get_by_matricola(999999)
print(s2)