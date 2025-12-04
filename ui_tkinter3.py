"""
Tk inter 3
"""
import tkinter as tk

def on_click(event):
    print(f"{event.widget['text']} presionado")

ventana = tk.Tk()

buttons = [tk.Button(ventana, text=f"Boton {i}") for i in range(3) ]

for button in buttons:
    button.pack()
    button.bind("<Button-1>", on_click)

# Radio button

variable_control = tk.IntVar()  # Es necesaria una variable para relecionar distintas opciones de radio buttons
opcion1 = tk.Radiobutton(ventana, text="opcion 1", variable=variable_control, value=1)
opcion2 = tk.Radiobutton(ventana, text="opcion 2", variable=variable_control, value=2)

opcion1.pack()
opcion2.pack()

def mostrar_opcion():
    print(f"Opcion seleccionada:{variable_control.get()}")

boton_opcion = tk.Button(ventana, text="Mostrar selección", command=mostrar_opcion)

boton_opcion.pack()
variable_control_check = tk.IntVar()
def on_cambio_check():
    if variable_control_check.get():
        boton.config(state="normal")
    else:
        boton.config(state="disabled")

    
check = tk.Checkbutton(ventana, text="Habiloitar boton", variable=variable_control_check, command=on_cambio_check)
check.pack()
boton = tk.Button(ventana, text="prueba check", state="disabled")
boton.pack()

ventana.mainloop()