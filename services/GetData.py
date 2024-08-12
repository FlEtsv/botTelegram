import logging
import requests

from config.Routes import GETDATABOTNEW
from services.FormatData import format_api_response
from sesion import sesion


def getDataMenssage():
    try:
        sesion_instance = sesion.Sesion()
        if not sesion_instance.ip_port:
            raise ValueError("IP port is not set in the session instance")

        logging.info(f"Using IP port: {sesion_instance.ip_port}")
        api_url = f'http://{sesion_instance.ip_port}/api/get_data_bot'
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        message = format_api_response(data)
        return message
    except requests.exceptions.RequestException as e:
        return f"Error en la conexion: {e}"
    except ValueError as e:
        return str(e)