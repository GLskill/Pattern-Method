#cross-platform GUI app

import abc
import platform
from typing import Protocol


class Window(Protocol):
    def __init__(self, title: str, width: int, height: int) -> None:
        self.title = title
        self.width = width
        self.height = height

    @abc.abstractmethod
    def draw(self) -> None:
        pass

    @abc.abstractmethod
    def set_size(self, width: int, height: int) -> None:
        pass

    def set_title(self, title: str) -> None:
        self.title = title

    def add(self, text_label):
        pass


class TextLabel(Protocol):
    def __init__(self, text: str) -> None:
        self.text = text

    @abc.abstractmethod
    def set_text(self, text: str) -> None:
        self.text = text


class TextInput(Protocol):
    def __init__(self) -> None:
        self.text = ""

    @abc.abstractmethod
    def get_text(self) -> str:
        return self.text

    @abc.abstractmethod
    def set_text(self, text: str) -> None:
        self.text = text


class Button(Protocol):
    @abc.abstractmethod
    def click(self) -> None:
        pass


class WindowsWindow(Window):
    def draw(self) -> None:
        print("Drawing Windows window...")

    def set_size(self, width: int, height: int) -> None:
        self.width = width
        self.height = height


class WindowsTextLabel(TextLabel):
    def set_text(self, text: str) -> None:
        self.text = text


class WindowsTextInput(TextInput):
    def get_text(self) -> str:
        return self.text

    def set_text(self, text: str) -> None:
        self.text = text


class WindowsButton(Button):
    def click(self) -> None:
        print("Windows button clicked!")


class GnomeWindow(Window):
    def draw(self) -> None:
        print("Drawing Gnome window...")

    def set_size(self, width: int, height: int) -> None:
        self.width = width
        self.height = height


class GnomeTextLabel(TextLabel):
    def set_text(self, text: str) -> None:
        self.text = text


class GnomeTextInput(TextInput):
    def get_text(self) -> str:
        return self.text

    def set_text(self, text: str) -> None:
        self.text = text


class GnomeButton(Button):
    def click(self) -> None:
        print("Gnome button clicked!")


class MacWindow(Window):
    def draw(self) -> None:
        print("Drawing Mac window...")

    def set_size(self, width: int, height: int) -> None:
        self.width = width
        self.height = height


class MacTextLabel(TextLabel):
    def set_text(self, text: str) -> None:
        self.text = text


class MacTextInput(TextInput):
    def get_text(self) -> str:
        return self.text

    def set_text(self, text: str) -> None:
        self.text = text


class MacButton(Button):
    def click(self) -> None:
        print("Mac button clicked!")


class GUI(Protocol):
    def create_window(self, title: str, width: int, height: int) -> Window:
        ...

    def create_text_label(self, text: str) -> TextLabel:
        ...

    def create_text_input(self, placeholder: str) -> TextInput:
        ...

    def create_button(self, text: str) -> Button:
        ...


class WindowsGUI:
    def create_window(self, title: str, width: int, height: int) -> Window:
        """initializing window creation"""
    def create_text_label(self, text: str) -> TextLabel:
        """initializing the creation of a text label in Windows"""
    def create_text_input(self, placeholder: str) -> TextInput:
        """implementations and creation of an input field in Windows"""
    def create_button(self, text: str) -> Button:
        """creating a button in windows"""


class GnomeGUI:
    def create_window(self, title: str, width: int, height: int) -> Window:
        """initializing Gnome creation"""
    def create_text_label(self, text: str) -> TextLabel:
        """initializing the creation of a text label in Gnome"""
    def create_text_input(self, placeholder: str) -> TextInput:
        """implementations and creation of an input field in Gnome"""
    def create_button(self, text: str) -> Button:
        """creating a button in Gnome"""


class MacGUI:
    def create_window(self, title: str, width: int, height: int) -> Window:
        """initializing mac creation"""
    def create_text_label(self, text: str) -> TextLabel:
        """initializing the creation of a text label in Mac"""
    def create_text_input(self, placeholder: str) -> TextInput:
        """implementations and creation of an input field in Mac"""
    def create_button(self, text: str) -> Button:
        """creating a button in Mac"""


def draw_greetings_screen(username: str, gui: GUI) -> None:
    window = gui.create_window(title="HELLOW", width=100, height=100)
    text_label = gui.create_text_label(text=f"Hi, {username}! Welcome to the new project",)
    window.add(text_label)
    window.draw()


def __main__():
    global gui
    os = platform.system()
    if os == "Windows":
        gui = WindowsGUI()
    elif os == "linux":
        gui = GnomeGUI()
    elif os == "Darwin":
        gui = MacGUI
    draw_greetings_screen(os.getlogin(), gui)






















