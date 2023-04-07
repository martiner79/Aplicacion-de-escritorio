
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#En este caso no es necesario usar nuestra ventana
'''
ventana_pr = tk.Tk()
ventana_pr.title("Proyecto - Aplicación")
ventana_pr.config(width=300, height=200)
'''

#Cuadros de diálogo

# Retornan TRUE o FALSE

messagebox.askokcancel(title="Pregunta", message="¿Desea seguir?")
messagebox.askyesno(title="Pregunta", message="¿Desea cancelar?")
messagebox.askretrycancel(title="Pregunta", message="¿Desea reintentar?")

# Retornan OK

messagebox.showinfo(title="Info", message="Se ha descargado el Programa")
messagebox.showwarning(title="Advertencia", message="Los programas de terceros pueden contener virus")
messagebox.showerror(title="Error", message="El siguiente sitio no es seguro.¿Desea seguir?")


#ventana_pr.mainloop()