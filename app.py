import logging
import os

from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler

from config.IpConfig import configuracionIpConfirmacion, configuracionIp, IP_PORT
from db.create_db import ObtenerConexion, obtenerToken
from evalue.branchEval import init
from flujo.flujoHelp import helpComand
from flujo.flujoObtencionDatos import  datos
from flujo.flujoVerficiacionNumero import start, PHONE_NUMBER, ComprobarTelefono, ComprobarCodigo, VERIFICATION_CODE

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Ensure the data directory exists
os.makedirs('data/historialDatos', exist_ok=True)

# Conectar a la base de datos SQLite
conn, cursor = ObtenerConexion()

def help(update, context):
    update.message.reply_text("This is the help message.")

def main() -> None:
    token = obtenerToken()
    if token is None:
        raise ValueError("Token no encontrado en la base de datos")
    application = Application.builder().token(token).build()

    conv_handler_start = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            PHONE_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, ComprobarTelefono)],
            VERIFICATION_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ComprobarCodigo)],
        },
        fallbacks=[CommandHandler("cancel", start)],
    )

    conv_handler_ip = ConversationHandler(
        entry_points=[CommandHandler("ip", configuracionIp)],
        states={
            IP_PORT: [MessageHandler(filters.TEXT & ~filters.COMMAND, configuracionIpConfirmacion)],
        },
        fallbacks=[CommandHandler("cancel", configuracionIp)],
    )

    conv_handler_datos = ConversationHandler(
        entry_points=[CommandHandler("datos", datos)],
        states={
        },
        fallbacks=[CommandHandler("cancel", datos)],
    )

    conv_handler_help = ConversationHandler(
        entry_points=[CommandHandler("help", helpComand)],
        states={
        },
        fallbacks=[CommandHandler("cancel", helpComand)],
    )

    application.add_handler(conv_handler_start)
    application.add_handler(conv_handler_ip)
    application.add_handler(conv_handler_datos)
    application.add_handler(conv_handler_help)
    application.run_polling()

if __name__ == '__main__':
    init()
    main()