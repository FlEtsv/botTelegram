from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from telegram.ext import Application

from db.create_db import comprobarVerificado
from services.GetData import getDataMenssage




async def datos(update: Update, context: CallbackContext) :
    if comprobarVerificado() == False:
        await update.message.reply_text("No puedes acceder a los datos hasta que no verifiques tu número de teléfono")
        return ConversationHandler.END
    menssage = getDataMenssage()
    await update.message.reply_text(menssage)
    return ConversationHandler.END


