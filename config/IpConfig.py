from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from services.conexion import pruebaConexion
from sesion import sesion

IP_PORT = range(1)

async def configuracionIp(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Necesito que me facilites la ip y puerto de donde has instalado la web de esta forma "192.168.1.1:8080"')
    return IP_PORT

async def configuracionIpConfirmacion(update: Update, context: CallbackContext) -> int:
    ip_port = update.message.text
    context.user_data['ip_port'] = ip_port
    await update.message.reply_text(f'La ip y puerto que has introducido es {ip_port}.')
    await update.message.reply_text('¿Es correcto? voy a comprobar que es correcto')
    return await configuracionIpComprobacion(update, context)

async def configuracionIpComprobacion(update: Update, context: CallbackContext) -> int:
    ip_port = context.user_data.get('ip_port')

    if pruebaConexion(ip_port):
        sesion_instance = sesion.Sesion()
        sesion_instance.ip_port = ip_port
        await update.message.reply_text(f'La ip y puerto introducida es correcta. se ha guardado en sesion {sesion_instance.ip_port} ')
        return ConversationHandler.END
    else:
        await update.message.reply_text('La ip y puerto introducida no es correcta, por favor, vuelva a introducirla.')
        return IP_PORT
