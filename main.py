import logging
from telegram import Update, ChatAction
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

state = 1
life = 3

updater = Updater(token="5713179669:AAFBc65fQz4X_PQU2ctokMWdiMBAZRdwJX0", use_context=True)
dispatcher = updater.dispatcher

def start_command_handler(update: Update, context: CallbackContext):
    global state
    if state == 1:
        context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!") 
        text = 'вітаю в грі "Хто це". Ну що ж розпочнемо'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        with open('chadwick_boseman.png', 'rb') as file:
            context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
            context.bot.send_photo(update.effective_chat.id, photo=file)
        text_1 = '''
1: Джон Вік
2: Кріс Еванс
3: Чедвік Боусман
'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_1)
        state += 1
    else:
        pass

def text_message_handler(update: Update, context: CallbackContext):
    message = update.message.text
    global state
    global life
    if state == 2 and life > 0:
        if message == '3':
            text = '''
1: Аліша Кіз
2: Люсі Хейл
3: Олівія Вайлд            
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('lucy_hale.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '1':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
        elif message == '2':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 3 and life > 0:
        if message == '2':
            text = '''
1: Аманда Байнс
2: Енн Хеч
3: Скарлет Йоханссон
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('anne_hatch.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '1':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
        elif message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 4 and life > 0:
        if message == '2':
            text = '''
1: Джекі Чан
2: Каньє Вест
3: Кіану Рівз
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('jackie_chan.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '1':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
        elif message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 5 and life > 0:
        if message == '1':
            text = '''
1: Вілл Сміт
2: Курт Рассел
3: Мыккы Рурк
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('will_smith.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '2':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
        elif message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 6 and life > 0:
        if message == '1':
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір")
            state += 1
        elif message == '2':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
        elif message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif life == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ви програли. Щоб спробувати ще раз напишіть /start")
        state /= state
        life += 3
    else:
        pass

start_handler = CommandHandler('start', start_command_handler)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler)
dispatcher.add_handler(echo_handler)

# Start bot
updater.start_polling()