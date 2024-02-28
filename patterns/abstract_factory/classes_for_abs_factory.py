from abc_classes import Window, TextInput, TextLabel, Button


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


