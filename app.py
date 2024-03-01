import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Digifico
---
Ejercicio: parcial
---
Enunciado:
De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos
Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso ( entre 100 y 800)
Tipo de material ( aluminio, hierro , madera)
Costo en $ (mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue tipo de material más usado ( aluminio, hierro , madera)
Informe B- El porcentaje de contenedores de Categoría peligroso
Informe C- La marca y tipo del contenedor más pesado
Informe D- La marca del contenedor de comestible con menor costo
Informe E- El promedio de costo de todos los contenedores de Hierro

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        CANTIDAD_ITERACIONES = 20
        contador_aluminio = 0
        contador_hierro = 0
        contador_madera = 0 
        acumulador_materiales = 0
        contador_peligroso = 0
        contador_comestible = 0
        contador_indumentaria = 0
        acumulador_tipo = 0
        marca_nombre = ""
        tipo_mas_pesado = ""
        mas_pesado = 99
        menor_costo_comestible = 1
        nombre_marca_comestible = ""
        contador_costo_hierro = 0
        acumulador_costo_hierro = 0

        for i in range(CANTIDAD_ITERACIONES):
            marca = prompt("Marca", "Indicar nombre de la marca")

            categoría = prompt("Categoria", "Indicar categoria(peligroso, comestible o indumentaria)").lower()
            while categoría != "peligroso" and categoría != "comestible" and categoría != "indumentaria":
                categoría = prompt("Error", "Por favor, indicar correctamente la categoria (peligroso, comestible o indumentaria)")

            peso = prompt("Peso", "Indicar peso del contenedor")
            while not peso.isdigit() or int(peso) < 100 or int(peso) > 800:
                peso = prompt("Error", "Por favor, indicar peso correctamente")

            tipo_material = prompt("material", "Indicar tipo de material (aluminio, hierro o madera)")
            while tipo_material != "aluminio" and tipo_material != "hierro" and tipo_material != "madera":
                tipo_material = prompt("Error", "Por favor, indicar correctamente el material")

            costo = prompt("Costo", "Indicar costo del contenedor")
            while not costo.isdigit() or int(costo) < 0:
                costo = prompt("Error", "Por favor, ingresar un costo valido")

            if tipo_material == "madera":
                contador_madera += 1
            if tipo_material == "hierro":
                contador_hierro += 1

            if tipo_material == "aluminio":
                contador_aluminio += 1

            if categoría == "comestible":
                contador_comestible += 1
            if categoría == "peligroso":
                contador_peligroso += 1
            if categoría == "indumentaria":
                contador_indumentaria += 1

            if int(peso) > mas_pesado:
                mas_pesado = int(peso)
                marca_nombre = marca
                tipo_mas_pesado = tipo_material

            if categoría == "comestible":
                if menor_costo_comestible == 1 or int(costo) < menor_costo_comestible:
                   menor_costo_comestible = int(costo)
                   nombre_marca_comestible = marca

            if (tipo_material == "hierro"):
                acumulador_costo_hierro += int(costo)
                contador_costo_hierro += 1
            
        if(contador_costo_hierro != 0):
            promedio_costos = acumulador_costo_hierro / contador_costo_hierro
        else:
            promedio_costos = 0
            print("El promedio de costos del hierro es: {0}".format(promedio_costos))
        
        if contador_madera > contador_aluminio and contador_madera > contador_hierro:
            acumulador_materiales = "madera"
        elif contador_aluminio > contador_hierro and contador_aluminio > contador_madera:
            acumulador_materiales = "aluminio"
        elif contador_hierro > contador_madera and contador_hierro > contador_aluminio:
            acumulador_materiales = "hierro"
        else:
            print("Materiales", "No hay mayoria")
          
        print("El material mas utilizado fue", acumulador_materiales)

        acumulador_materiales = contador_indumentaria + contador_comestible + contador_peligroso
        porcentaje_peligroso = (contador_peligroso / acumulador_materiales) * 100

        print("Porcentaje peligroso", porcentaje_peligroso)

        print("La marca mas pesada es: ", marca_nombre)
        print("Tipo", tipo_mas_pesado)
        print("Peso", mas_pesado)

        if nombre_marca_comestible != "":
            print("La marca comestible de menor costo es: ", nombre_marca_comestible)
            print("Costo:", menor_costo_comestible)
        else:
            print("No ingresaron productos comestibles")
  
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()