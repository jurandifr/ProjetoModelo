#!/usr/bin/python3
"""
Projeto Modelo

Exemplo de Interface

UI source file: pygubu.ui
"""
import tkinter as tk
import tkinter.ttk as ttk


def safe_i18n_translator(value):
    """i18n - Setup translator in derived class file"""
    return value


def safe_fo_callback(widget):
    """on first objec callback - Setup callback in derived class file."""
    pass


def safe_image_loader(master, image_name: str):
    """Image loader - Setup image_loader in derived class file."""
    img = None
    try:
        img = tk.PhotoImage(file=image_name, master=master)
    except tk.TclError:
        pass
    return img


class interfaceUI:
    def __init__(
        self,
        master=None,
        *,
        translator=None,
        on_first_object_cb=None,
        data_pool=None,
        image_loader=None
    ):
        if translator is None:
            translator = safe_i18n_translator
        _ = translator  # i18n string marker.
        if image_loader is None:
            image_loader = safe_image_loader
        if on_first_object_cb is None:
            on_first_object_cb = safe_fo_callback
        # build ui
        self.tk1 = tk.Tk(master)
        self.tk1.configure(height=200, width=400)
        self.tk1.resizable(False, False)
        self.tk1.title("Projeto Modelo")
        # First object created
        on_first_object_cb(self.tk1)

        self.label1 = ttk.Label(self.tk1)
        self.label1.configure(text='label1')
        self.label1.pack(expand=True, side="top")
        self.button1 = ttk.Button(self.tk1)
        self.button1.configure(text='executar')
        self.button1.pack(padx=8, pady=8, side="bottom")
        self.button1.configure(command=self.executar)
        self.tk1.pack_propagate(0)

        # Main widget
        self.mainwindow = self.tk1

    def run(self):
        self.mainwindow.mainloop()

    def executar(self):
        pass


if __name__ == "__main__":
    app = interfaceUI()
    app.run()
