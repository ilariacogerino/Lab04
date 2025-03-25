import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # PAGE
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # CONTROLLER
        self._controller = None

        # UI ELEMENTS

        self._title = None
        self._theme_switch = None
        self._ddLingua = None
        self._ddTipoRicerca = None
        self._txtIn = None
        self._btnSpellCheck = None
        self._frase = None
        self._txtOut = None


    def add_content(self):

        #AGGIUNTA DELLO SWITCH E DEL TITOLO
        self._title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self._theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        row1 = ft.Row(controls=[self._theme_switch, self._title], spacing = 30, alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row1)

        #AGGIUNTA DEL MENU' A TENDINA PER LA SCELTA DELLA LINGUA
        self._ddLingua = ft.Dropdown(label = "Select language",
                               options=[ft.dropdown.Option("english"), ft.dropdown.Option("italian"), ft.dropdown.Option("spanish")],
                                     on_change = self.controlloSelezione)
        self.page.add(self._ddLingua)

        #AGGIUNTA DEL MENU' A TENDINA PER IL TIPO DI RICERCA, DELLA FRASE E DEL BOTTONE PER EFFTUARE LA RICERCA
        self._ddTipoRicerca = ft.Dropdown(label = "Search modality",
                                    options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"), ft.dropdown.Option("Dichotomic")],
                                          on_change = self.controlloSelezione)

        self._txtIn = ft.TextField(label = "Add your sentence here")
        self._btnSpellCheck = ft.ElevatedButton(text = "Spell check", on_click = self.handleSpellCheck)
        row3 = ft.Row(controls = [self._ddTipoRicerca, self._txtIn, self._btnSpellCheck], alignment = ft.MainAxisAlignment.CENTER)
        self.page.add(row3)

        #AGGIUNTA DELA LISTVIEW PER SCRIVERE LE COSE DAL CONTROLLER
        self._txtOut = ft.ListView()
        self._txt = ft.Text("", visible=False)
        self.page.add(self._txtOut, self._txt)

        self.page.update()

    def handleSpellCheck(self, e):
        risultato = self._controller.handleSentence(str(self._txtIn.value), self._ddLingua.value, self._ddTipoRicerca.value)
        if self._txtIn.value == "":
            self._txtOut.controls.append(ft.Text(f"Inserire un valore non nullo!"))
        else:
            self._txtOut.controls.append(ft.Text(f"Frase inserita: {self._txtIn.value}"))
            self._txtOut.controls.append(ft.Text(f"Parole errate: {risultato[0]}"))
            self._txtOut.controls.append(ft.Text(f"Tempo richiesto dall ricerca: {risultato[1]}"))

        self._txtIn.value=""
        self.page.update()

    def controlloSelezione(self, e):
        if self._ddLingua.value:
            self._txt.value = f'Selezione corretta della lingua'
            self._txt.color = "green"
        self._txt.visible = True

        if self._ddTipoRicerca.value:
            self._txt.value = f'Selezione corretta della modalità'
            self._txt.color = "green"
        self._txt.visible = True

        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self._controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self._theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
