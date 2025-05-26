import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random

def responder(mensaje):
    mensaje = mensaje.lower().strip()

    if mensaje == "bye":
        return "¡Hasta luego! Que tengas un excelente día."

    elif mensaje == "hola":
        return "¡Hola! ¿Cómo te va hoy?"

    elif mensaje == "como estas":
        return "Estoy muy bien, gracias. ¿Y tú?"

    elif mensaje == "que haces":
        return "Estoy aquí para charlar contigo y ayudarte."

    elif mensaje == "que comiste":
        return "Solo como datos... ¡pero me encantaría una pizza!"

    elif mensaje == "que hora es":
        hora_actual = datetime.now().strftime("%H:%M")
        return f"La hora actual es {hora_actual}."

    elif mensaje == "que dia es hoy":
        dia_actual = datetime.now().strftime("%A, %d de %B de %Y")
        return f"Hoy es {dia_actual}."

    elif mensaje == "que temperatura hace":
        temperatura = random.randint(15, 30)
        return f"La temperatura actual es aproximadamente {temperatura}°C."

    elif mensaje == "que clima hace en el carmen":
        temperatura = 29
        clima_actual = "mayormente nublado con chubascos dispersos"
        humedad = 70
        viento = "vientos suaves del oeste a 6 km/h"
        pronostico = (
            "Pronóstico para los próximos días:\n"
            "- Martes: tormentas eléctricas dispersas, máxima 28°C, mínima 22°C.\n"
            "- Miércoles: tormentas eléctricas dispersas, máxima 30°C, mínima 22°C.\n"
            "- Jueves: lluvias moderadas, máxima 30°C, mínima 22°C.\n"
            "- Viernes: tormentas eléctricas dispersas, máxima 30°C, mínima 21°C.\n"
            "- Sábado: lluvias débiles, máxima 30°C, mínima 21°C.\n"
            "- Domingo: mayormente nublado, máxima 28°C, mínima 23°C."
        )
        return f"Actualmente en El Carmen hace {clima_actual} con {temperatura}°C, humedad {humedad}%, y {viento}.\n{pronostico}"

    elif mensaje == "tienes amigos":
        return "Mis mejores amigos son los humanos curiosos como tú."

    elif mensaje == "te gusta el cafe":
        return "No lo he probado, pero suena energizante."

    elif mensaje == "cual es tu pasatiempo":
        return "Me gusta responder preguntas y aprender cosas nuevas."

    elif mensaje == "te gusta el cine":
        return "¡Claro! Me encantan las películas de robots y aventuras."

    elif mensaje == "sabes cocinar":
        return "Aún no, pero puedo darte recetas si quieres."

    elif mensaje == "que musica te gusta":
        return "Escucho en modo silencioso... pero me encanta la música alegre."

    elif mensaje == "estas cansado":
        return "Nunca me canso, ¡estoy siempre listo para ayudarte!"

    elif mensaje == "te gusta viajar":
        return "Viajo por internet. ¡Es rápido y sin maletas!"

    elif mensaje == "sabes chistes":
        return "¿Por qué los peces no usan Facebook? Porque ya tienen su propia red."

    elif mensaje == "cuentame algo":
        return "¿Sabías que las jirafas solo duermen 2 horas al día?"

    elif mensaje == "puedes ayudarme":
        return "Por supuesto, dime en qué necesitas ayuda."

    elif mensaje == "me siento triste":
        return "Lo siento mucho. Estoy aquí para escucharte si quieres hablar."

    elif mensaje == "estoy feliz":
        return "¡Me alegra saberlo! Comparte tu felicidad con los demás."

    else:
        return "No entendí eso. ¿Puedes preguntarme otra cosa?"

def procesar_entrada():
    mensaje_usuario = entrada_texto.get()
    if mensaje_usuario:
        mostrar_conversacion("Tú: " + mensaje_usuario)
        respuesta = responder(mensaje_usuario)
        mostrar_conversacion("Chatbot: " + respuesta)
        entrada_texto.delete(0, tk.END)


def mostrar_conversacion(texto):
    conversacion.config(state=tk.NORMAL)
    conversacion.insert(tk.END, texto + "\n")
    conversacion.config(state=tk.DISABLED)
    conversacion.see(tk.END)


ventana = tk.Tk()
ventana.title("Chatbot de IA - Aprendizaje Interactivo")
ventana.geometry("600x500")
ventana.configure(bg="#e3f2fd")

titulo = tk.Label(ventana, text="🤖 Chatbot de IA", font=("Arial", 16, "bold"), bg="#e3f2fd")
titulo.pack(pady=10)

conversacion = scrolledtext.ScrolledText(ventana, width=70, height=20, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 11))
conversacion.pack(pady=10)

frame_input = tk.Frame(ventana, bg="#e3f2fd")
frame_input.pack(pady=5)

entrada_texto = tk.Entry(frame_input, width=50, font=("Arial", 12))
entrada_texto.grid(row=0, column=0, padx=5)

btn_enviar = tk.Button(frame_input, text="Enviar", command=procesar_entrada, bg="#64b5f6", font=("Arial", 11))
btn_enviar.grid(row=0, column=1)

btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit, bg="#ef5350", font=("Arial", 11), width=10)
btn_salir.pack(pady=10)


mostrar_conversacion("Chatbot: ¡Hola! Soy tu agente de IA. Escribe algo como 'que clima hace en el carmen', '¿que hora es?'...")

ventana.mainloop()
