import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def handleLanguage(self, e):
        self._view.__txtOut.controls.append(
            ft.Text(value="Language correctly selected: " + self._view.__ddLanguage.value))
        self._view.page.update()


    def handleModality(self, e):
        self._view.__txtOut.controls.append(
            ft.Text(value="Search modality correctly selected: " + self._view.__ddModality.value))
        self._view.page.update()


    def handleSpellCheck(self, e):
        sentence = self._view.__txtInt.value
        if sentence == "":
            self._view.__txtOut.controls.clear()
            self._view.__txtOut.controls.append(ft.Text(value="Add a sentence!"))
            return
        language = self._view.__ddLanguage.value
        modality = self._view.__ddModality.value
        if language == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select language!"))
            return
        if modality == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select modality!"))
            return

        words, elapsedTime = self.handleSentence(sentence, language, modality)

        self._view.__txtOut.controls.clear()
        self._view.__txtOut.controls.append(ft.Text("Sentence : " + sentence))
        self._view.__txtOut.controls.append(ft.Text("Errors: " + words))
        self._view.__txtOut.controls.append(ft.Text(value="Elapsed time: " + str(elapsedTime)))

        self._view.page.update()


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text