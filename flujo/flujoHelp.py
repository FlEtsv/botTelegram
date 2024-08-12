from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler


async def helpComand(update: Update, context: CallbackContext) :

    await update.message.reply_text(
        "Puedes usar los siguientes comandos:\n"
        "/start - Inicia la conversación (inicia verificación)\n"
        "/datos - Muestra los datos (solo verificados)\n"
        "/ip - Configura la ip y puerto (verificación de ip)\n"
        "/help - Muestra esta ayuda"
    )
    return ConversationHandler.END