# importamos del archivo env.py el path donde se alojan los archivos y el token generado por la creacion del bot en telegram
#Aqui en el inicio del programa dejare las instrucciones para la creacion del bot en Telegram

# Primero, cree un bot usando Telegram BotFather. Para crear un BotFather, siga los pasos a continuación: 
# Abra la aplicación Telegram y busque @BotFather.
# Haz clic en el botón de inicio o envía “/start”.
# Luego envíe el mensaje «/newbot» para configurar un nombre y un nombre de usuario.
# Después de configurar el nombre y el nombre de usuario, BotFather le dará un token de API que es su token de bot. 
# Ir al bot de telegram y escribir /start
# Ir a la url https://api.telegram.org/bot[token]/getUpdates con el token previo 
# Crear grupo de telegram donde se incluya la cuenta del bot creado
# De la nueva url extraemos el chatid, lo ultimo despues del # https://web.telegram.org/k/#-844761121

from env import token, path
import requests, datetime

# Ahora realizaremos la peticion enviando en el msg tipos de archvos
img = f"{path}logo.png"
mp3 = f"{path}cancion.mp3"
pdf = f"{path}sample.pdf"
api = f"https://api.telegram.org/bot{token}"
chatid = "-844761121"

def bot_send_text():
    # estos son los parametros minimos necesarios para q el bot acepte la peticion de envio de msg
    params = {
        "chat_id": chatid,
        "parse_mode": "HTML",
        "text": f"{datetime.datetime.now()} funcionando..."
    }
    # Aqui hacemos la peticion de tipo post
    response = requests.post(f"{api}/sendMessage", params=params)
    # Aqui mostramos el resultado de la peticion
    print("Response => ", response.content)

def bot_send_file(archivo):
    params = {
        "chat_id": chatid
    }
    files = {
        "document": open(archivo, "rb"),
        "caption": "picture.png"
    }
    response = requests.post(f"{api}/sendDocument", params=params, files=files)
    print("Response post => ", response.content)

if __name__ == "__main__":
    bot_send_text()
    bot_send_file(img)
    bot_send_file(mp3)
    bot_send_file(pdf)