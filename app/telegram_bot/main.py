from emoji import demojize
from telebot import TeleBot, types
from module import *

PATH_TO_TEMPORARY_FILE = './temporaty_files/'
TOKEN = '7866695394:AAE4VA7z_q-cMLtbhXrr_euzH2tqloCjreI'
START_MESSAGE = '''
*Добро пожаловать в умный и простой сервис для сравнения документов\\!*

Здравствуйте, я — ваш цифровой помощник, созданный для того, чтобы превращать сложную задачу анализа текстов в лёгкий, быстрый и доступный процесс\\.

Если вам нужна помощь со стартом, то выберете команду "/help", для просмотра информации о командах\\.

Моя задача — сократить время для поиска документации и ваши нервы:\\) 
'''
HELP_MESSAGE = '''
*Команды бота:*

\\- _/help_ – это команда, которая выводит информацию о командах\\.P\\.s\\. вы её сейчас смотрите;

\\- _/start_ – это команда, которая выводит начальное сообщение и описывает с чем могу помочь;

\\- _/change\\_count\\_documents_ – это команда, которая изменяет количество документов, которое вы хотите получить на выходе;

\\- _/find\\_documents_ – это команда, которая находит схожие документы, введённые вами строкой; 
'''
HOW_TO_FIND_DOCUMENTS = '''
    Для поиска документов, необходимо ввести любую строку и спустя время я их вам выдам.
'''

count_documents = 1
bot=TeleBot(TOKEN)
user_states = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    user_states[message.chat.id] = 'start'
    bot.send_message(message.chat.id, START_MESSAGE, parse_mode="MarkdownV2")

@bot.message_handler(commands=['help'])
def help_message(message):
    user_states[message.chat.id] = 'help'
    bot.send_message(message.chat.id, HELP_MESSAGE, parse_mode="MarkdownV2")

@bot.message_handler(commands=['change_count_documents'])
def change_count_documents(message):
    user_states[message.chat.id] = 'change_count_documents'
    markup = types.InlineKeyboardMarkup()
    markup.add(*[types.InlineKeyboardButton(f'{i+1}', callback_data=f'btn_change_count_documents|{i+1}') for i in range(10)])
    bot.send_message(message.chat.id, f"На данный момент у вас количество документов для отправки ({count_documents}). Выберете новое количество документов для отправки:", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data and callback.data.startswith('btn_change_count_documents'))
def callback_change_count_document(callback: types.CallbackQuery):
    # user_states[callback.from_user.id] = 'change_count_documents'
    new_count = callback.data.split('|')[1]
    id = callback.from_user.id
    if not new_count.isdigit() or (id not in user_states and user_states[id] != 'change_count_documents'):
        return
    
    global count_documents

    new_count = int(new_count)
    count_documents = new_count
    bot.send_message(callback.from_user.id, f'Количество отправляемых документов успешно изменено на ({count_documents}).')

@bot.message_handler(commands=['find_documents'])
def find_documents(message):
    user_states[message.chat.id] = 'find_documents'
    bot.send_message(message.chat.id, HOW_TO_FIND_DOCUMENTS)

@bot.message_handler(content_types=['text'])
def get_documents(message):
    if message.chat.id not in user_states or user_states[message.chat.id] not in ['wait_response_documents', 'find_documents']:
        bot.send_message(message.chat.id, 'Извините, я вас не понял:(\nМожете ввести команду "\\help" или выбрать из меню, чтобы узнать о возможностях бота.')
        return
        
    if user_states[message.chat.id] == 'wait_response_documents':
        bot.send_message(message.chat.id, 'Идёт поиск документов. Пожалуйста подождите!')

    elif user_states[message.chat.id] == 'find_documents':
        if len(message.text) != len(demojize(message.text)):
            bot.send_message(message.chat.id, 'Извините, но для поиска документов нельзя использовать эмоджи!')
            return
        
        user_states[message.chat.id] = 'wait_response_documents'
        bot.send_message(message.chat.id, 'Начало поиска документов...')
        documents = request_api(f'documents/?text={message.text}&count_documents={count_documents}')
        
        if 'error' in documents:
            user_states[message.chat.id] = 'find_documents'
            bot.send_message(message.chat.id, 'К сожалению поиск документов временно не работает. Мы стараемся быстрее это исправить.')
            return

        for document in documents:
            path = f'{PATH_TO_TEMPORARY_FILE}{document['name_file']}'
            save_temporary_file(path, document['document'])

            with open(path, 'rb') as file:
                bot.send_document(message.chat.id, file, caption=formatting_output_data_API(document))

            deleted_temporary_file(path)
        user_states[message.chat.id] = 'find_documents'

if __name__ == '__main__':
    bot.infinity_polling()