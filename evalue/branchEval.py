# evalue/branchEval.py
import threading
import time
import asyncio
from telegram import Bot
from db.create_db import obtenerToken, obtenerChatId
from evalue.Evalue import Ver_evaluarDatos, evaluarFechaHora, recuperar_evaluarConfiguracion
from sesion import sesion
import threading



bot = Bot(token=obtenerToken())


async def send_message_async(bot, chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)


async def send_telegram_message(message):
    bot = Bot(token=obtenerToken())
    await bot.send_message(chat_id=obtenerChatId(), text=message)




def action():
    while True:
        mensaje = ""
        # Perform the desired action here
        data = Ver_evaluarDatos()
        if evaluarFechaHora(data):
            voltaje_limit, VoltajeIs_active = recuperar_evaluarConfiguracion(name="voltaje")
            autonomia_limit, autonomiaIs_active = recuperar_evaluarConfiguracion(name="autonomia")
            temperatura_limit, temperaturaIs_active = recuperar_evaluarConfiguracion(name="temperatura")
            bateria_limit, bateriaIs_active = recuperar_evaluarConfiguracion(name="bateria")
            kilometraje_limit, kilometrajeIs_active = recuperar_evaluarConfiguracion(name="kilometraje")

            if VoltajeIs_active:
                if data["voltaje"] < voltaje_limit:
                    mensaje += f"Alerta el valor de voltaje es {data['voltaje']}\n"
            if autonomiaIs_active:
                if data["autonomia"] < autonomia_limit:
                    mensaje += f"Alerta el valor de autonomia es {data['autonomia']}\n"
            if temperaturaIs_active:
                if data["temperatura"] > temperatura_limit:
                    mensaje += f"Alerta el valor de temperatura es {data['temperatura']}\n"
            if bateriaIs_active:
                if data["nivel"] < bateria_limit:
                    mensaje += f"Alerta el valor de nivel de bateria es {data['nivel']}\n"
            if kilometrajeIs_active:
                if data["kilometros"] > kilometraje_limit:
                    mensaje += f"Alerta el valor de kilometraje es {data['kilometros']}\n"

            if mensaje:
                asyncio.run(send_telegram_message(mensaje))

        time.sleep(60)


def init():
    action_thread = threading.Thread(target=action)
    action_thread.daemon = True  # This makes the thread exit when the main program exits
    action_thread.start()