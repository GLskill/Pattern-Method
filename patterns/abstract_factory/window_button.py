import tkinter as tk
from tkinter import messagebox


class CrossPlatformApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cross-Platform App")

        self.label = tk.Label(root, text="Hello")
        self.label.pack(pady=10)

        self.button = tk.Button(root, text="Click Me, FAST", command=self.show_message)
        self.button.pack(pady=30)

    def show_message(self):
        messagebox.showinfo("Message", "You clicked the button")


def main():
    root = tk.Tk()
    app = CrossPlatformApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()