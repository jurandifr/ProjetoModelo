#!/usr/bin/python3
"""
Projeto Modelo

Exemplo de Interface

UI source file: pygubu.ui
"""
import tkinter as tk
import tkinter.ttk as ttk
import desktopui as baseui


class interface(baseui.interfaceUI):
    def __init__(self, master=None):
        super().__init__(master)

    def executar(self):
        pass


if __name__ == "__main__":
    app = interface()
    app.run()
