import tkinter as tk
import util.generic as utl
from tkinter import ttk
from tkinter.font import BOLD


class FormRegisterDesigner:
    
    def register(self):
        pass

    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title('Registro de usuario')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 600, 450)

        # frame logo
        logo = utl.leer_imagen("./img/logo.png", (200, 200))
        frame_logo = tk.Frame(self.ventana, bd=0, width=200, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side='left', expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # frame form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand= tk.YES, fill=tk.BOTH)
        
        # frame form top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de usuario", font=('Times', 30), fg='#666a88', bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        # frame form fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=15, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=15, pady=5)
        
        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=15, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=15, pady=5)
        self.password.config(show='*')
        
        etiqueta_confirmacion = tk.Label(frame_form_fill, text="Confirmar Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_confirmacion.pack(fill=tk.X, padx=15, pady=5)
        self.confirmacion = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.confirmacion.pack(fill=tk.X, padx=15, pady=5)
        self.confirmacion.config(show='*')
        
        
        registro = tk.Button(frame_form_fill, text="Registrar", font=('Times',15), bg='#F87474', bd=0, fg='#3a7ff6', command=self.register)
        registro.pack(fill=tk.X, padx=15, pady=20)
        registro.bind("<Return>", (lambda event:self.register()))
        
        self.ventana.mainloop()