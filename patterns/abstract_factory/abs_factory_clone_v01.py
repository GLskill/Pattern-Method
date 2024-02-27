import platform
from gui_clasesses import WindowsGUI, GnomeGUI, MacGUI
from gui_abs_classes import GUI


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


