import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Lautaro
apellido: Melana
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador_de_interacciones = 0
        while contador_de_interacciones < 10:
            contador_de_interacciones += 2
            print(contador_de_interacciones)
    
        alert("FIN", "La suma es 2,4,6,8 y 10")
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()