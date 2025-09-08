import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # Controller
        self.__controller = None

        # UI elements
        self.__title = None
        self.__theme_switch = None
        self.__ddLanguage = None
        self.__ddModality = None
        self.__txtInt = None
        self.__btnSpellCheck = None
        self.__txtOut = None


    def add_content(self):
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        row1 = ft.Row(controls=[self.__theme_switch, self.__title], spacing=30, alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row1)

        # select language
        self.__ddLanguage = ft.Dropdown(label="Select Language",
                                        options=[ft.DropdownOption("english"), ft.DropdownOption("italian"), ft.DropdownOption("spanish")],
                                        on_change=self.__controller.handleLanguage)
        self.page.add(self.__ddLanguage)

        # modality + txtIn + Spell check button
        self.__ddModality = ft.Dropdown(label="Search Modality",
                                        options=[ft.DropdownOption("Contains"), ft.DropdownOption("Linear"), ft.DropdownOption("Dichotomic")],
                                        on_change=self.__controller.handleModality)
        self.__txtInt = ft.TextField(label="Add your sentence here")
        self.__btnSpellCheck = ft.ElevatedButton(text="Spell Check",
                                                 on_click=self.__controller.handleSpellCheck)
        row2 = ft.Row(controls=[self.__ddModality, self.__txtInt, self.__btnSpellCheck])
        self.page.add(row2)

        # listview to write from controller
        self.__txtOut = ft.ListView(expand=1, spacing=10)
        self.page.add(self.__txtOut)


        self.page.update()


    def update(self):
        self.page.update()


    def setController(self, controller):
        self.__controller = controller


    def theme_changed(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        self.page.update()