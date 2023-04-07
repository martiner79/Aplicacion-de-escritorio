
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#La primera parte será especificar la estructura los detalles de nuestra ventana

ventana_pr = tk.Tk()
ventana_pr.title("Proyecto - Aplicación")
ventana_pr.config(width=300, height=200)

#Barras de progreso

# Barra Horizontal

barra = ttk.Progressbar(maximum=100)
barra.place(x=10, y=10, width=100)
barra.step(50)
barra.start(50)

# Barra vertical

barra = ttk.Progressbar(orient=tk.VERTICAL, maximum=100)
barra.place(x=10, y=50, height=100)
barra.start(20)


ventana_pr.mainloop()