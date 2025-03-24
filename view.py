import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # PAGE
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # CONTROLLER
        self.__controller = None

        # UI ELEMENTS
        self.__title = None
        self.__theme_switch = None
        self.__ddLingua = None
        self.__ddTipoRicerca = None
        self.__txtIn = None
        self.__btnSpellCheck = None
        self.__frase = None
        self.__txtOut = None

    def add_content(self):

        #AGGIUNTA DELLO SWITCH E DEL TITOLO
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        row1 = ft.Row(controls=[self.__theme_switch, self.__title], spacing = 30, alignment=ft.MainAxisAlignment.START)
        self.page.add(row1)

        #AGGIUNTA DEL MENU' A TENDINA PER LA SCELTA DELLA LINGUA
        self.__ddLingua = ft.Dropdown(label = "Select language",
                               options=[ft.dropdown.Option("english"), ft.dropdown.Option("italian"), ft.dropdown.Option("spanish")])
        self.page.add(self.__ddLingua)

        #AGGIUNTA DEL MENU' A TENDINA PER IL TIPO DI RICERCA, DELLA FRASE E DEL BOTTONE PER EFFTUARE LA RICERCA
        self.__ddTipoRicerca = ft.Dropdown(label = "Search modality",
                                    options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"), ft.dropdown.Option("Dichotomic")])
        self.__txtIn = ft.TextField(label = "Add your sentance here")
        self.__btnSpellCheck = ft.ElevatedButton(text = "Spell check", on_click = self.__controller.handleSentence(self.__txtIn.value, self.__ddLingua.value, self.__ddTipoRicerca.value))
        row3 = ft.Row(controls = [self.__ddTipoRicerca, self.__txtIn, self.__btnSpellCheck])
        self.page.add(row3)

        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
