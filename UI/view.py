import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        #UI elements
        self.dd_corso = None
        self.btn_iscritti = None

        self.txt_matricola = None
        self.txt_nome = None
        self.txt_cognome = None

        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None
        self.btn_iscrivi = None

        self.txt_result = None

    def set_controller(self, controller):
        self._controller = controller

    def load_interface(self):
        title = ft.Text("Segreteria studenti", color="blue", size="24")
        self._page.controls.append(title)

        # Row 1: Dropdown corso + bottone Cerca iscritti
        self.dd_corso = ft.Dropdown(label="Corso", width=520)
        self.btn_iscritti = ft.ElevatedButton(
            text="Cerca iscritti",
            on_click=self._controller.handle_cerca_iscritti
        )
        self._page.controls.append(
            ft.Row([self.dd_corso, self.btn_iscritti], alignment=ft.MainAxisAlignment.CENTER)
        )

        # Row 2: Matricola + Nome + Cognome (read-only)
        self.txt_matricola = ft.TextField(label="Matricola", width=150)
        self.txt_nome = ft.TextField(label="Nome", width=220, read_only=True)
        self.txt_cognome = ft.TextField(label="Cognome", width=220, read_only=True)

        self._page.controls.append(
            ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome],
                   alignment=ft.MainAxisAlignment.CENTER))

        # Row 3: bottoni Cerca studente / Cerca corsi / Iscrivi (opzionale)
        self.btn_cerca_studente = ft.ElevatedButton(
            text="Cerca studente",
            on_click=self._controller.handle_cerca_studente
        )
        self.btn_cerca_corsi = ft.ElevatedButton(
            text="Cerca corsi",
            on_click=self._controller.handle_cerca_corsi
        )
        self.btn_iscrivi = ft.ElevatedButton(
            text="Iscrivi",
            on_click=self._controller.handle_iscrivi
        )
        self._page.controls.append(
            ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi],
                   alignment=ft.MainAxisAlignment.CENTER)
        )

        # Row 4: ListView risultati
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True, height=320)
        self._page.controls.append(self.txt_result)
        self._page.update()

    def clear_result(self):
        self.txt_result.controls.clear()
        self._page.update()

    def clear_results(self):
        self.clear_result()

    def add_result_lines(self, lines):
        for line in lines:
            self.txt_result.controls.append(ft.Text(line))
        self._page.update()

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def fill_corsi_dropdown(self, corsi):
        self.dd_corso.options.clear()
        for corso in corsi:
            self.dd_corso.options.append(
                ft.dropdown.Option(key=corso.codins, text=str(corso))
            )
        self._page.update()