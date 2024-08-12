# Define the module `config/routes.py`
from sesion import sesion

# Base URL
BASE_URL = f"http://{sesion.Sesion.ip_port}"

# User-related routes
CONEXION = f"{BASE_URL}/api/alive"

GETDATABOTNEW = f"{BASE_URL}/api/get_data_bot"
