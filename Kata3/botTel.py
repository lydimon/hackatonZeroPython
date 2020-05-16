from telegram.ext import Updater, CommandHandler

def main():
    #instanciamos el updater
    #updater = Updater(token=open("./bot_token").read(), use_context=True)
    updater = Updater(token="1194275450:AAEmYXSfRtWWSlOrkmq6O185Gzw5wWW-Q5o", use_context=True)
    
    #añadiendo un manejador al comando start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #empezamos a pedir notificaciones a Telegram
    updater.start_polling()

    #capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola, soy un bot")

main()