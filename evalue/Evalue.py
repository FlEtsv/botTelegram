import json
import os
from datetime import datetime

from services.getConfig import getConfig
from sesion import sesion


def Ver_evaluarDatos():
    historical_data = []

    if os.path.exists('data/historialDatos/historical_data.json'):
        with open('data/historialDatos/historical_data.json', 'r') as f:
            try:
                historical_data = json.load(f)

            except json.JSONDecodeError:
                print("Error decodificando historical_data.json")
                historical_data = []
        # Encontrar la entrada más reciente
        entrada_mas_reciente = max(historical_data, key=lambda x: datetime.fromisoformat(x["timestamp"]))

        # Extraer el timestamp más reciente
        fecha_hora = entrada_mas_reciente["timestamp"]

        # Extraer y asignar los valores de "data" a variables con el mismo nombre
        data = entrada_mas_reciente["data"]
        battery_voltage = data["battery_voltage"]
        autonomy = data["autonomy"]
        charging_mode = data["charging_mode"]
        charging_status = data["charging_status"]
        level = data["level"]
        air_temp = data["air_temp"]
        luminosity_day = data["luminosity_day"]
        acceleration = data["acceleration"]
        speed = data["speed"]
        preconditioning_status = data["preconditioning_status"]
        mileage = data["mileage"]

        # Crear un diccionario con los valores extraídos
        datos = {
            "voltaje": battery_voltage,
            "autonomia": autonomy,
            "nivel": level,
            "temperatura": air_temp,
            "kilometros": mileage,
            "timestamp": fecha_hora
        }
        return datos

def evaluarFechaHora(datos) -> bool:
    fecha_hora = datos["timestamp"]
    fecha_hora = datetime.fromisoformat(fecha_hora)
    if sesion.Sesion().fecha is None:
        sesion.Sesion().fecha = fecha_hora.isoformat()
        print("Fecha guardada")
        return True
    elif fecha_hora > datetime.fromisoformat(sesion.Sesion().fecha):
        sesion.Sesion().fecha = fecha_hora.isoformat()
        print("Fecha actualizada")
        return True
    else:
        print("Fecha igual o menor")
        return False

# evalue/Evalue.py
def recuperar_evaluarConfiguracion(name: str):
    config_data = getConfig(name)
    if not config_data or config_data.startswith("Error"):
        print(f"Error: Config data for {name} is empty or invalid.")
        return None, None

    try:
        data = json.loads(config_data)  # Ensure data is a dictionary
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON for {name}: {e}")
        return None, None

    if data:
        value_limit = data["value_limit"]
        is_active = bool(data["is_active"])  # Convert to boolean
        return value_limit, is_active
    else:
        return None, None










