import logging
from telegram import Update

from telegram.ext import CallbackContext, ConversationHandler

from db.create_db import obtenerCodigoVerificacion, obtenerTelefono, darComoVerificado, eliminarCodigoVerificacion, \
    añadirChatId
from evalue import branchEval
from evalue.branchEval import init
from sesion import sesion

PHONE_NUMBER, VERIFICATION_CODE = range(2)

sesion_instance = sesion.Sesion()

async def start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Bienvenido! Por favor, envíame tu número de teléfono.')
    return PHONE_NUMBER


async def ComprobarTelefono(update: Update, context: CallbackContext) -> int:
    phone_number = update.message.text
    chat_id = update.message.chat_id
    añadirChatId(chat_id)
    logging.info(f'Añadido chat id: {chat_id}')
    logging.info(f'Received phone number: {phone_number}')
    logging.info(f'Chat ID: {chat_id}')
    try:
        phone_number = int(phone_number)
    except ValueError:
        await update.message.reply_text('Por favor, introduce un número de teléfono válido.')
        return PHONE_NUMBER  # Return to the same state to re-enter the phone number

    logging.info(f'Converted phone number to int: {phone_number}')

    db_phone_number = obtenerTelefono()
    logging.info(f'Phone number from database: {db_phone_number}')

    if len(str(phone_number)) != 9:
        logging.info('Phone number does not have exactly 9 digits.')
        await update.message.reply_text('Por favor, introduce un número de teléfono válido.')
        return PHONE_NUMBER  # Return to the same state to re-enter the phone number

    if db_phone_number != str(phone_number):
        logging.info('Phone number is already in the database.')
        await update.message.reply_text('Este número de teléfono ya está registrado.')
        return PHONE_NUMBER  # Return to the same state to re-enter the phone number

    context.user_data['phone_number'] = phone_number
    context.user_data['chat_id'] = chat_id
    await update.message.reply_text(
        f'Gracias por enviarme tu número de teléfono: {phone_number}. Ahora, por favor, envíame el código de verificación.')
    return VERIFICATION_CODE
async def ComprobarCodigo(update: Update, context: CallbackContext) -> int:
    verification_code = update.message.text
    phone_number = context.user_data.get('phone_number')
    chat_id = context.user_data.get('chat_id')
    logging.info(f'Chat ID: {chat_id}')
    try:
        verification_code = int(verification_code)
    except ValueError:
        await update.message.reply_text('Por favor, introduce un código de verificación válido.')
        return VERIFICATION_CODE  # Return to the same state to re-enter the verification code

    # Verificar el código de verificación
    if verification_code == int(obtenerCodigoVerificacion()):
        await update.message.reply_text(f'Tu número de teléfono {phone_number} ha sido verificado con éxito.')
        darComoVerificado()
        eliminarCodigoVerificacion()
        return ConversationHandler.END


    await update.message.reply_text('Código de verificación incorrecto. Por favor, inténtalo de nuevo.')
    return VERIFICATION_CODE



