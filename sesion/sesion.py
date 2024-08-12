# sesion/sesion.py
import logging
import threading

class Sesion:
    _instance = None
    __lock = threading.Lock()
    _chat_id = None
    _ip_port = None
    _fecha = None

    def __new__(cls):
        if cls._instance is None:
            with cls.__lock:
                if cls._instance is None:
                    cls._instance = super(Sesion, cls).__new__(cls)
        return cls._instance

    @property
    def chat_id(self):
        with self.__lock:
            return self._chat_id

    @chat_id.setter
    def chat_id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("El chat_id debe ser un entero")
        with self.__lock:
            self._chat_id = value

    @property
    def ip_port(self):
        with self.__lock:
            return self._ip_port

    @ip_port.setter
    def ip_port(self, value: str):
        if not isinstance(value, str):
            raise ValueError("El ip_port debe ser un string")
        with self.__lock:
            self._ip_port = value

    @property
    def fecha(self):
        with self.__lock:
            return self._fecha

    @fecha.setter
    def fecha(self, value: str):
        if not isinstance(value, str):
            raise ValueError("La fecha debe ser un string")
        with self.__lock:
            self._fecha = value

