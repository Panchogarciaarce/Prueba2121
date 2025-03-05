import os
import requests
import datetime
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = os.getenv("TOKEN")

def convertir_fecha_a_timestamp(fecha_str):
    """Convierte una fecha en formato YYYY-MM-DD a timestamp en milisegundos."""
    fecha_dt = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
    timestamp = int(fecha_dt.timestamp() * 1000)
    return timestamp

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("👋 ¡Hola! Envíame /buscar ORIGEN DESTINO YYYY-MM-DD para buscar pasajes en Smiles.")

async def buscar(update: Update, context: CallbackContext):
    if len(context.args) < 3:
        await update.message.reply_text("⚠️ Formato incorrecto. Usa: `/buscar ORIGEN DESTINO YYYY-MM-DD`")
        return

    origen, destino, fecha = context.args
    fecha_timestamp = convertir_fecha_a_timestamp(fecha)

    await update.message.reply_text(f"🔍 Buscando pasajes de **{origen}** a **{destino}** para el **{fecha}**... 🚀")

    url = f"https://www.smiles.com.ar/emission?originAirportCode={origen}&destinationAirportCode={destino}&departureDate={fecha_timestamp}&adults=1&children=0&infants=0&isFlexibleDateChecked=false&tripType=1&cabinType=all&currencyCode=BRL"

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Ajustar estos selectores según el HTML real de Smiles
        vuelos = soup.find_all("div", class_="flight-option")  # Ver si esta clase es correcta en Smiles

        if vuelos:
            resultados = "\n".join(
                [f"✈️ {vuelo.find('span', class_='route').text} - {vuelo.find('span', class_='price').text} millas" for vuelo in vuelos]
            )
            await update.message.reply_text(f"✅ Pasajes encontrados:\n{resultados}")
        else:
            await update.message.reply_text("❌ No encontramos pasajes disponibles en Smiles.")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error al buscar vuelos: {e}")

# Configurar el bot
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buscar", buscar))

if __name__ == "__main__":
    app.run_polling()
