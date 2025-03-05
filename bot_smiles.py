import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Configurar logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# Obtener el Token del bot desde las variables de entorno
TOKEN = os.getenv("BOT_TOKEN")

# Función de inicio
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("👋 ¡Hola! Envíame /buscar ORIGEN DESTINO FECHA para buscar pasajes en Smiles.")

# Función para buscar pasajes (simulación)
async def buscar(update: Update, context: CallbackContext):
    if len(context.args) < 3:
        await update.message.reply_text("⚠️ Formato incorrecto. Usa: `/buscar ORIGEN DESTINO FECHA`")
        return

    origen, destino, fecha = context.args
    await update.message.reply_text(f"🔍 Buscando pasajes de **{origen}** a **{destino}** para el **{fecha}**... 🚀")

    # Aquí iría la lógica para consultar Smiles
    await update.message.reply_text("❌ No encontramos pasajes disponibles en Smiles.")

# Configurar la aplicación de Telegram
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buscar", buscar))

# Configurar Webhook en Render
PORT = int(os.environ.get("PORT", 8443))

        if __name__ == "__main__":
    app.run_polling()
    )
