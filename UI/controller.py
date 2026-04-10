import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def load_data(self):
        corsi = self._model.load_corsi()
        self._view.fill_corsi_dropdown(corsi)

    def _get_matricola(self):
        raw = self._view.txt_matricola.value

        if raw is None or raw.strip() == "":
            return None

        raw = raw.strip()

        if not raw.isdigit():
            return -1

        return int(raw)

    def handle_cerca_iscritti(self, e):
        self._view.clear_results()

        if self._view.dd_corso.value is None:
            self._view.create_alert("Seleziona un corso prima di cercare gli iscritti.")
            return

        codins = self._view.dd_corso.value
        iscritti = self._model.get_iscritti_corso(codins)

        if len(iscritti) == 0:
            self._view.add_result_lines([f"Nessun iscritto trovato per il corso {codins}."])
            return

        lines = [f"Iscritti al corso {codins}: {len(iscritti)} studenti"]
        for s in iscritti:
            lines.append(str(s))

        self._view.add_result_lines(lines)

    def handle_cerca_studente(self, e):
        self._view.clear_results()

        m = self._get_matricola()
        if m is None:
            self._view.create_alert("Inserisci una matricola.")
            return
        if m == -1:
            self._view.create_alert("Matricola non valida. Inserisci solo numeri.")
            return

        stud = self._model.get_studente(m)
        if stud is None:
            self._view.create_alert("Matricola non presente nel database.")
            self._view.txt_nome.value = ""
            self._view.txt_cognome.value = ""
            self._view.update_page()
            return

        self._view.txt_nome.value = stud.nome
        self._view.txt_cognome.value = stud.cognome
        self._view.update_page()

        self._view.add_result_lines([f"Trovato: {stud}"])

    def handle_cerca_corsi(self, e):
        self._view.clear_results()

        m = self._get_matricola()
        if m is None:
            self._view.create_alert("Inserire una matricola.")
            return
        if m == -1:
            self._view.create_alert("Matricola non presente nel database.")
            return

        stud = self._model.get_studente(m)
        if stud is None:
            self._view.create_alert("Matricola non presente nel database.")
            return

        corsi = self._model.get_corsi_studente(m)
        if len(corsi) == 0:
            self._view.add_result_lines([f"{stud} non è iscritto a nessun corso."])
            return

        lines = [f"Corsi di {stud}:"]
        for c in corsi:
            lines.append(str(c))

        self._view.add_result_lines(lines)


    def handle_iscrivi(self, e):
        self._view.clear_results()

        if self._view.dd_corso.value is None:
            self._view.create_alert("Seleziona un corso prima di iscriverti.")
            return

        codins = self._view.dd_corso.value

        m = self._get_matricola()
        if m is None:
            self._view.create_alert("Inserire una matricola.")
            return
        if m == -1:
            self._view.create_alert("Matricola non valida: usa solo numeri.")
            return

        stud = self._model.get_studente(m)
        if stud is None:
            self._view.create_alert("Matricola non presente nel database.")
            return

        ok = self._model.iscrivi(m, codins)
        if not ok:
            self._view.create_alert("Iscrizione fallita (forse lo studente è già iscritto a quel corso).")
            return

        self._view.add_result_lines([f"Iscrizione completata: {stud} -> {codins}"])
