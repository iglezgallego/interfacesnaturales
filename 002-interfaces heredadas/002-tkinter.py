##Este programa ilustra el concepto de GUI, Graphical user interface, interfaz gráfica con ventanas
##Aparece la libreria de interfaz gráfica tkinter
import tkinter as tk
raiz = tk.Tk()
##Introduzco widgets en este caso un boton
tk.Button(raiz,text="Pulsame").pack(padx=20,pady=20)

raiz.mainloop()
