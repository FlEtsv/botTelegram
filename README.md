# Bot Telegram 🤖

## Descripción  
Este proyecto consiste en el desarrollo de un bot en Python utilizando la librería python-telegram-bot (Telegram.ext) con autenticación de usuarios. El bot está diseñado para monitorear y notificar en tiempo real cualquier cambio en una web existente. Se integra con la ***web [SensorStats](https://github.com/FlEtsv/sensorStats)***, autentica usuarios de manera segura y envía notificaciones automáticas a través de Telegram sobre actualizaciones relevantes en los datos mostrados en la web. Esta implementación permite una interacción fluida y eficiente con los usuarios, asegurando que reciban las últimas actualizaciones directamente en sus dispositivos móviles.

## Requisitos previos
> ⚠️ *Advertencia: El producto principal es la web **[SensorStats](https://github.com/FlEtsv/sensorStats)***. Es necesario instalarla y ponerla en funcionamiento antes de instalar o iniciar el bot.

Para utilizar correctamente este bot, se debe instalar junto con la ***web [SensorStats](https://github.com/FlEtsv/sensorStats)***. Una vez completada la instalación y registro del bot, siga los siguientes pasos:

1. Asegúrese de tener Docker y Docker Compose instalados en su sistema.
2. Descargue la imagen del bot desde Docker Hub.
3. Cree un contenedor utilizando la imagen descargada.
4. Asigne un nombre al contenedor.
5. En el apartado de volúmenes, añada un nuevo volumen que requerirá dos rutas:
   - La primera ruta debe coincidir con la ruta asignada al volumen durante la instalación de la ***web [SensorStats](https://github.com/FlEtsv/sensorStats)***.
   - La segunda ruta debe ser /app/data/historialDatos.

6. El bot estará listo para comenzar su configuración.

## Notas antes de la configuración
- El bot se configura principalmente desde el chat, excepto en lo que respecta a la configuración de las alertas.
- Si el bot se reinicia, se perderá la configuración del comando /ip.
- Para ver la lista de comandos disponibles, utilice el comando /help.
- Descargue la versión fletsv/bottelegram:latest si desea que WatchTower actualice automáticamente la imagen del bot.

## Funcionalidades
El bot ofrece dos funciones principales:

1. *Recolección de datos en tiempo real:* Utilizando el comando /datos, el bot devolverá un conjunto de datos actualizados en ese momento.
2. *Configuración de alertas desde la web:* A través del menú del bot, se pueden habilitar las alertas deseadas entre las disponibles. En esta función, el bot monitorea los datos existentes en la página, lo que puede generar un retraso de hasta 3 horas en el monitoreo (recopilación automática de datos periódica). Para evitar este retraso, se puede solicitar una actualización de datos manualmente utilizando el comando /datos, lo que actualizará el registro y permitirá al bot detectar los datos más recientes.

## Instalación
El bot se puede clonar directamente desde este repositorio. Es posible utilizarlo de la misma manera que la web, como un script genérico compartiendo directorios del sistema. Está diseñado para ser utilizado en un entorno Docker.
