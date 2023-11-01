import tkinter as tk
import util.generic as utl
from forms.form_master import MasterPanel
from tkinter import ttk, messagebox
from tkinter.font import BOLD


class app:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)