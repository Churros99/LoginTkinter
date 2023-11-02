from forms.registration.form_designer import FormRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_User
from tkinter import messagebox
import util.encoding_decoding as end_dec
import tkinter as tk

class FormRegister(FormRegisterDesigner):
    
    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()
        
    def register(self):
        if(self.isConfirmationPassword()):
            user = Auth_User()
            user.username = self.usuario.get()
            user_db: Auth_User = self.auth_repository.getUserByUserName(self.usuario.get())
            if not (self.isUserRegister(user_db)):
                user.password = end_dec.encrypted(self.password.get())
                self.auth_repository.insertUser(user)
                messagebox.showinfo(message="Se registro el usuario", title="Mensaje")
    
    def isConfirmationPassword(self):
        status:bool = True
        if(self.password.get() != self.confirmacion.get()):
            status = False
            messagebox.showerror(message="La contraseña no coinciden por favor verifica el registro", title="Mensaje")
            self.password.delete(0,tk.END)
            self.confirmacion.delete(0, tk.END)
        
        return status
    
    def isUserRegister(self, user:Auth_User):
        status:bool = False
        if(user != None):
            status = True
            messagebox.showerror(message="El Usuario ya existe", title="Mensaje")
        
        return status