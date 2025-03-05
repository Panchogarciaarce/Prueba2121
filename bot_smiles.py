import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Configurar logging para ver errores en Render
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# Obtener el Token del bot desde las variables de entorno
TOKEN = os.getenv("TOKEN")

# Función de inicio
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("👋 ¡Hola! Enviame /buscar ORIGEN DESTINO FECHA para buscar pasajes en Smiles.")

# Función para buscar pasajes
async def buscar(update: Update, context: CallbackContext):
    if len(context.args) < 3:
        await update.message.reply_text("⚠️ Formato incorrecto. Usa: `/buscar ORIGEN DESTINO FECHA`")
        return

    origen, destino, fecha = context.args
    await update.message.reply_text(f"🔎 Buscando pasajes de **{origen}** a **{destino}** para el **{fecha}**... 🚀")

    # Aquí debería ir la lógica real para consultar Smiles

    await update.message.reply_text("❌ No encontramos pasajes disponibles en Smiles.")

# Configurar la aplicación de Telegram
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buscar", buscar))

# Ejecutar el bot con polling (SIN WEBHOOKS)
if __name__ == "__main__":
    app.run_polling()
