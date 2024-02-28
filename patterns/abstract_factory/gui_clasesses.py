from gui_abs_classes import GUI
from abc_classes import TextInput, TextLabel, Button
from classes_for_abs_factory import Window, WindowsWindow, WindowsButton, WindowsTextLabel, WindowsTextInput
from classes_for_abs_factory import GnomeWindow, GnomeButton, GnomeTextLabel, GnomeTextInput
from classes_for_abs_factory import MacWindow, MacButton, MacTextLabel, MacTextInput


class WindowsGUI(GUI):
    def create_window(self, title: str, width: int, height: int) -> Window:
        return WindowsWindow(title, width, height)

    def create_text_label(self, text: str) -> TextLabel:
        return WindowsTextLabel(text)

    def create_text_input(self, placeholder: str) -> TextInput:
        return WindowsTextInput()

    def create_button(self, text: str) -> Button:
        return WindowsButton()


class GnomeGUI(GUI):
    def create_window(self, title: str, width: int, height: int) -> Window:
        return GnomeWindow(title, width, height)

    def create_text_label(self, text: str) -> TextLabel:
        return GnomeTextLabel(text)

    def create_text_input(self, placeholder: str) -> TextInput:
        return GnomeTextInput()

    def create_button(self, text: str) -> Button:
        return GnomeButton()


class MacGUI(GUI):
    def create_window(self, title: str, width: int, height: int) -> Window:
        return MacWindow(title, width, height)

    def create_text_label(self, text: str) -> TextLabel:
        return MacTextLabel(text)

    def create_text_input(self, placeholder: str) -> TextInput:
        return MacTextInput()

    def create_button(self, text: str) -> Button:
        return MacButton()


