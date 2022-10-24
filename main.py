import logging
from telegram import Update, ChatAction
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters
from db import users_collection
import uuid

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

state = 1
life = 5

updater = Updater(token="5713179669:AAHkXRSX2X_mrw9ZVDfU-lmtDtOBcSRkh_k", use_context=True)
dispatcher = updater.dispatcher

def start_command_handler(update: Update, context: CallbackContext):
    user_by_id = users_collection.find_one({"_id": update.effective_chat.id})
    
    global state
    
    if user_by_id != None:
        print("User already exists")
    else:
        print("New user")
        user = {
            "_id": update.effective_chat.id,
            "name": update.effective_chat.full_name,
            "user_state": [state]
        }
        users_collection.insert_one(user)

    
    if state == 1:
        context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Привіт, {update.effective_chat.first_name}!") 
        text = 'вітаю в грі "Хто це". Памятайте в вас всього 5 житів. Ну що ж розпочнемо'
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
        elif message == '1' or message == '2':
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
        elif message == '1' or message == '3':
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
        elif message == '1' or message == '3':
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
        elif message == '2' or message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 6 and life > 0:
        if message == '1':
            text = '''
1: Анна Адамович
2: Анна Кошмал
3: Даша Плахтый
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('anna_koshmal.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '2' or message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 7 and life > 0:
        if message == '2':
            text = '''
1: Раян Рейнольдс
2: Кріс Еванс
3: Бенедикт Камбербетч
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('benedict_cumberbatch.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '1' or message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 8 and life > 0:
        if message == '3':
            text = '''
1: Стас Боклан
2: Андрій Федінчик
3: Тарас Cтадницький
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('andriy_fedinchyk.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '1' or message == '2':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 9 and life > 0:
        if message == '2':
            text = '''
1: Кріс Гемсворт
2: Том Холанд
3: Кріс Еванс
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('chris_hemsworth.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '1' or message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 10 and life > 0:
        if message == '1':
            text = '''
1: Гарік Бірча
2: Михайло Досенко
3: Сергій Анипченко
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('garik_bircha.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '2' or message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 11 and life > 0:
        if message == '1':
            text = '''
1: Ендрю Гарфілд
2: Тобі Магваєр
3: Зак Ефрон
'''
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. А хто це")
            with open('andrew_garfield.png', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
        elif message == '2' or message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif state == 12 and life > 0:
        if message == '1':
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю правильний вибір. Гру завершено якщо хочете зіграти ще раз пропишіть /start")
            state = 1
        elif message == '2' or message == '3':
            text = "Неправильно. Подумайте ще"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            life -= 1
    elif life == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ви програли. Щоб спробувати ще раз напишіть /start")
        state = 1
        life = 5
    else:
        pass

start_handler = CommandHandler('start', start_command_handler)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler)
dispatcher.add_handler(echo_handler)

# Start bot
updater.start_polling()