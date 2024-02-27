import abc
from abc_classes import Window, TextInput, TextLabel, Button


class GUI(abc.ABC):
    @abc.abstractmethod
    def create_window(self, title: str, width: int, height: int) -> Window:
        pass

    @abc.abstractmethod
    def create_text_label(self, text: str) -> TextLabel:
        pass

    @abc.abstractmethod
    def create_text_input(self, placeholder: str) -> TextInput:
        pass

    @abc.abstractmethod
    def create_button(self, text: str) -> Button:
        pass


