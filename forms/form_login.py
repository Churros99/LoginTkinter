import tkinter as tk
import util.generic as utl
from forms.form_master import MasterPanel
from tkinter import ttk, messagebox
from tkinter.font import BOLD


class App:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)

        # frame logo
        logo = utl.leer_imagen("./img/logo.png", (200, 200))
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side='left', expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # frame form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand= tk.YES, fill=tk.BOTH)
        
        # frame form top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=('Times', 30), fg='#666a88', bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.ventana.mainloop()