from tkinter import Tk, Button, Entry
import re

# Configuración ventana principal
root = Tk()
root.title("Calculadora")
root.resizable(0,0)
root.geometry("300x250")

def clickBoton_0():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "0")
def clickBoton_1():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "1")
def clickBoton_2():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "2")
def clickBoton_3():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "3")
def clickBoton_4():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "4")
def clickBoton_5():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "5")
def clickBoton_6():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "6")
def clickBoton_7():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "7")
def clickBoton_8():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "8")
def clickBoton_9():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "9")
def clickBoton_punto():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + ".")
def clickBoton_mas():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "+")
def clickBoton_menos():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "-")
def clickBoton_multiplicacion():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "*")
def clickBoton_division():
    texto_actual = pantalla.get()
    pantalla.delete(0, 'end')
    pantalla.insert(0, texto_actual + "/")
def clickBoton_igual():
    texto_actual = pantalla.get()
    operacion = re.split("(\+|\-|\*|\/)", texto_actual)
    resultado = float(operacion[0])
    for index, i in enumerate(operacion):
        if i == "+":
            resultado += float(operacion[index+1])
        elif i == "-":
            resultado -= float(operacion[index+1])
        elif i == "*":
            resultado *= float(operacion[index+1])
        elif i == "/":
            resultado /= float(operacion[index+1])
    pantalla.delete(0, 'end')
    pantalla.insert(0, str(resultado))

#pantalla.grid(row=0, column=0, columnspan=8, padx=1, pady=1)

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=55, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", command = clickBoton_1, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", command = clickBoton_2, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", command = clickBoton_3, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", command = clickBoton_4, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", command = clickBoton_5, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", command = clickBoton_6, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", command = clickBoton_7, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", command = clickBoton_8, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", command = clickBoton_9, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", command = clickBoton_igual, width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", command = clickBoton_punto, width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", command = clickBoton_mas, width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", command = clickBoton_menos , width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", command = clickBoton_multiplicacion,  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", command = clickBoton_division, width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, columnspan=1, padx=1, pady=1)

root.mainloop()