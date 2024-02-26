import abc
import platform


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


class WindowsWindow(Window):
    def draw(self) -> None:
        print("Drawing Windows window...")

    def set_size(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def add(self, text_label) -> None:
        print("Adding Text Label to Windows Window...")


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

    def add(self, text_label) -> None:
        print("Adding Text Label to Gnome Window...")


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

    def add(self, text_label) -> None:
        print("Adding Text Label to Mac Window...")


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


def draw_greetings_screen(username: str, gui: GUI) -> None:
    window = gui.create_window(title="HELLO", width=100, height=100)
    text_label = gui.create_text_label(text=f"Hi, {username}! Welcome to the new project",)
    window.add(text_label)
    window.draw()


def main():
    os = platform.system()
    if os == "Windows":
        gui = WindowsGUI()
    elif os == "Linux":
        gui = GnomeGUI()
    elif os == "Darwin":
        gui = MacGUI()
    else:
        raise NotImplementedError(f"GUI for '{os}' is not implemented.")
    draw_greetings_screen(os, gui)


if __name__ == "__main__":
    main()