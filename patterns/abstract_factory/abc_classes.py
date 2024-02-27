import abc


class Window(abc.ABC):
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

    @abc.abstractmethod
    def add(self, text_label) -> None:
        pass


class TextLabel(abc.ABC):
    def __init__(self, text: str) -> None:
        self.text = text

    @abc.abstractmethod
    def set_text(self, text: str) -> None:
        pass


class TextInput(abc.ABC):
    def __init__(self) -> None:
        self.text = ""

    @abc.abstractmethod
    def get_text(self) -> str:
        pass

    @abc.abstractmethod
    def set_text(self, text: str) -> None:
        pass


class Button(abc.ABC):
    @abc.abstractmethod
    def click(self) -> None:
        pass


