from model.model import Model

m = Model()
corsi = m.load_corsi()
print("corsi:", len(corsi), corsi[0])

stud = m.get_studente(146101)
print("stud:", stud)

iscritti = m.get_iscritti_corso(corsi[0].codins)
print("iscritti primo corso:", len(iscritti))