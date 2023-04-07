

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



#La primera parte será especificar la estructura los detalles de nuestra ventana

ventana_pr = tk.Tk()
ventana_pr.title("Proyecto - Aplicación")
ventana_pr.config(width=300, height=200)

# Casilla de verificación (Checkbox)


def boton_checkbox():
    boton = bool.get()
    print(boton)


bool = tk.BooleanVar()
checkbutton = ttk.Checkbutton(text="Aceptar términos y condiciones", variable=bool)
checkbutton.place(x=10, y=10)
bool.set("False")

boton = ttk.Button(text="aceptar", command=boton_checkbox)
boton.place(x=10, y=40)


#Imagen dentro de etiqueta

'''
imagen = tk.PhotoImage(file="C:/directory/image")

label = ttk.Label(image=imagen)
label.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
'''

ventana_pr.mainloop()