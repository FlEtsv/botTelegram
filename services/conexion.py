import requests

from config.Routes import CONEXION
from sesion.sesion import Sesion


def pruebaConexion(ip_port):
    try:
        # Ensure the URL has the correct scheme
        if not ip_port.startswith(('http://', 'https://')):
            ip_port = f'http://{ip_port}'

        response = requests.get(f"{ip_port}/api/alive")
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        if data.get('status') == 'alive':
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error during connection: {e}")
        return False
