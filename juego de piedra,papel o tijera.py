import tkinter as tk
from tkinter import messagebox
import random

# Variables globales
puntos_jugador = 0
puntos_pc = 0
puntos_pc2 = 0
nombre_jugador = ""
num_oponentes = 1

# Función para validar el nombre (solo letras)
def validar_nombre(event):
    texto = entry_nombre.get()
    if not texto.isalpha():
        entry_nombre.delete(0, tk.END)
        messagebox.showerror("Error", "Por favor, ingresa un nombre válido (solo letras).")

# Función para iniciar el juego
def iniciar_juego():
    global nombre_jugador
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showerror("Error", "El campo del nombre no puede estar vacío.")
        return
    nombre_jugador = nombre
    ventana_nombre.destroy()
    ventana_oponentes()

# Función para elegir oponentes
def ventana_oponentes():
    ventana_op = tk.Tk()
    ventana_op.title("Seleccionar Oponentes")
    ventana_op.geometry("300x200")
    ventana_op.configure(bg="#FFFACD")  # Fondo amarillo pastel

    label_opciones = tk.Label(ventana_op, text="¿Contra cuántos oponentes quieres jugar?", font=("Arial", 12), bg="#FFFACD")
    label_opciones.pack(pady=10)

    btn_uno = tk.Button(ventana_op, text="1 PC", font=("Arial", 12), bg="#FFCC99", command=lambda: iniciar_partida(1, ventana_op))
    btn_uno.pack(pady=5)

    btn_dos = tk.Button(ventana_op, text="2 PCs", font=("Arial", 12), bg="#FFCC99", command=lambda: iniciar_partida(2, ventana_op))
    btn_dos.pack(pady=5)

    ventana_op.mainloop()

# Función para iniciar la partida
def iniciar_partida(oponentes, ventana_anterior):
    global num_oponentes, puntos_jugador, puntos_pc, puntos_pc2
    puntos_jugador = 0
    puntos_pc = 0
    puntos_pc2 = 0
    ventana_anterior.destroy()  # Cierra la ventana de selección de oponentes
    num_oponentes = oponentes
    pantalla_principal()

# Función principal del juego
def pantalla_principal():
    def jugar(opcion_jugador):
        global puntos_jugador, puntos_pc, puntos_pc2
        opciones = ["Piedra", "Papel", "Tijera"]
        eleccion_pc = random.choice(opciones)
        eleccion_pc2 = random.choice(opciones) if num_oponentes == 2 else None

        resultado = ""
        if eleccion_pc == opcion_jugador:
            resultado = "Empate con PC 1."
            puntos_jugador += 1
            puntos_pc += 1
        elif (opcion_jugador == "Piedra" and eleccion_pc == "Tijera") or \
             (opcion_jugador == "Papel" and eleccion_pc == "Piedra") or \
             (opcion_jugador == "Tijera" and eleccion_pc == "Papel"):
            resultado = "Ganaste contra PC 1."
            puntos_jugador += 2
        else:
            resultado = "Perdiste contra PC 1."
            puntos_pc += 2

        if num_oponentes == 2:
            if eleccion_pc2 == opcion_jugador:
                resultado += " Empate con PC 2."
                puntos_jugador += 1
                puntos_pc2 += 1
            elif (opcion_jugador == "Piedra" and eleccion_pc2 == "Tijera") or \
                 (opcion_jugador == "Papel" and eleccion_pc2 == "Piedra") or \
                 (opcion_jugador == "Tijera" and eleccion_pc2 == "Papel"):
                resultado += " Ganaste contra PC 2."
                puntos_jugador += 2
            else:
                resultado += " Perdiste contra PC 2."
                puntos_pc2 += 2

        actualizar_puntaje()
        resultado_label.config(text=resultado)
        if (num_oponentes == 1 and puntos_jugador < 10 and puntos_pc < 10) or (num_oponentes == 2 and puntos_jugador < 25 and puntos_pc < 25 and puntos_pc2 < 25):
            siguiente_partida_button.pack(pady=10)
        else:
            verificar_ganador()

    def actualizar_puntaje():
        marcador.config(text=f"{nombre_jugador}: {puntos_jugador} | PC 1: {puntos_pc}" +
                             (f" | PC 2: {puntos_pc2}" if num_oponentes == 2 else ""))

    def verificar_ganador():
        if puntos_jugador >= (10 if num_oponentes == 1 else 25):
            resultado_final = f"¡Felicidades, {nombre_jugador}! Ganaste la partida."
        elif puntos_pc >= (10 if num_oponentes == 1 else 25):
            resultado_final = "¡Perdiste la partida! PC 1 ha ganado."
        elif puntos_pc2 >= 25:
            resultado_final = "¡Perdiste la partida! PC 2 ha ganado."
        else:
            resultado_final = "¡Empate! Nadie ganó."

        resultado_label.config(text=resultado_final)
        boton_reiniciar.pack(pady=10)
        boton_salir.pack(pady=10)
        boton_regresar.pack(pady=10)

    # Interfaz de la partida
    ventana_juego = tk.Tk()
    ventana_juego.title("Piedra, Papel o Tijera")
    ventana_juego.geometry("700x600")
    ventana_juego.configure(bg="#FFFACD")  # Fondo amarillo pastel

    label_bienvenida = tk.Label(ventana_juego, text=f"Ha empezado el juego: {nombre_jugador} vs " +
                                                     ("PC 1 y PC 2" if num_oponentes == 2 else "PC 1"),
                                font=("Arial", 12), bg="#FFFACD")
    label_bienvenida.pack(pady=10)

    mensaje_ganador = tk.Label(ventana_juego, text="El que consiga primero 25 puntos gana la ronda." if num_oponentes == 2 else "El que consiga primero 10 puntos gana la ronda.", font=("Arial", 12, "italic"), bg="#FFFACD")
    mensaje_ganador.pack(pady=5)

    marcador = tk.Label(ventana_juego, text=f"{nombre_jugador}: 0 | PC 1: 0" +
                                            (f" | PC 2: 0" if num_oponentes == 2 else ""),
                        font=("Arial", 12, "italic"), bg="#FFFACD")
    marcador.pack(pady=5)

    resultado_label = tk.Label(ventana_juego, text="¡Haz tu elección!", font=("Arial", 12), bg="#FFFACD")
    resultado_label.pack(pady=10)

    frame_botones = tk.Frame(ventana_juego, bg="#FFFACD")
    frame_botones.pack(pady=10)

    btn_piedra = tk.Button(frame_botones, text="Piedra 🪨", font=("Arial", 12), bg="gray", fg="white", command=lambda: jugar("Piedra"))
    btn_piedra.grid(row=0, column=0, padx=5)

    btn_papel = tk.Button(frame_botones, text="Papel 📄", font=("Arial", 12), bg="white", fg="black", command=lambda: jugar("Papel"))
    btn_papel.grid(row=0, column=1, padx=5)

    btn_tijera = tk.Button(frame_botones, text="Tijera ✂️", font=("Arial", 12), bg="red", fg="white", command=lambda: jugar("Tijera"))
    btn_tijera.grid(row=0, column=2, padx=5)

    def siguiente_partida():
        resultado_label.config(text="¡Haz tu elección!")
        siguiente_partida_button.pack_forget()

    siguiente_partida_button = tk.Button(ventana_juego, text="Siguiente partida", font=("Arial", 12), bg="#ADD8E6", command=siguiente_partida)

    # Botones para salir, reiniciar y regresar
    def reiniciar_juego():
        global puntos_jugador, puntos_pc, puntos_pc2
        puntos_jugador = 0
        puntos_pc = 0
        puntos_pc2 = 0
        resultado_label.config(text="¡Haz tu elección!")
        marcador.config(text=f"{nombre_jugador}: 0 | PC 1: 0" + (f" | PC 2: 0" if num_oponentes == 2 else ""))
        boton_reiniciar.pack_forget()
        boton_salir.pack_forget()
        boton_regresar.pack_forget()
        siguiente_partida_button.pack_forget()

    boton_reiniciar = tk.Button(ventana_juego, text="Jugar otra vez", font=("Arial", 12), bg="#ADD8E6", command=reiniciar_juego)
    boton_salir = tk.Button(ventana_juego, text="Salir del juego", font=("Arial", 12), bg="#FF5733", command=ventana_juego.destroy)
    boton_regresar = tk.Button(ventana_juego, text="Regresar al menú", font=("Arial", 12), bg="#FFAA33", command=lambda: [ventana_juego.destroy(), ventana_oponentes()])

    ventana_juego.mainloop()


# Ventana inicial
ventana_nombre = tk.Tk()
ventana_nombre.title("Bienvenido")
ventana_nombre.geometry("400x300")
ventana_nombre.configure(bg="#FFFACD")

label_nombre = tk.Label(ventana_nombre, text="¿Cuál es tu nombre?", font=("Arial", 12), bg="#FFFACD")
label_nombre.pack(pady=10)

entry_nombre = tk.Entry(ventana_nombre, font=("Arial", 12))
entry_nombre.pack(pady=5)
entry_nombre.bind("<KeyRelease>", validar_nombre)

btn_continuar = tk.Button(ventana_nombre, text="Continuar", font=("Arial", 12), bg="#ADD8E6", command=iniciar_juego)
btn_continuar.pack(pady=10)

ventana_nombre.mainloop()
