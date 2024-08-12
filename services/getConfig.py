# services/getConfig.py
import json
import logging
import requests

import sesion.sesion

# services/getConfig.py
def getConfig(name: str):
    try:
        sesion_instance = sesion.sesion.Sesion()
        if not sesion_instance.ip_port:
            raise ValueError("IP port is not set in the session instance")

        logging.info(f"Using IP port: {sesion_instance.ip_port}")
        api_url = f'http://{sesion_instance.ip_port}/api/get_config_bot/{name}'
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        return json.dumps(data)  # Convert dictionary to JSON string
    except requests.exceptions.RequestException as e:
        return f"Error en la conexion: {e}"
    except ValueError as e:
        return str(e)