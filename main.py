import telebot
from Notes import Notes

notes = Notes()

bot = telebot.TeleBot('')


def text_without_com(message):
    return ' '.join(message.text.strip().split(' ')[1:])


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Список команд:
    Добавить заметку: /add
    Удалить заметку: /del
    Список заметок: /list
    Перейти в заметку: /choose
    Выйти из заметки: /exit
    Изменить название заметки: /name
    Добавить запись в заметку: /add_s
    Удалить записи из заметки: /del_s
    Просмотреть записи в заметке: /show''')


@bot.message_handler(commands=['add', 'добавить'])
def add_note(message):
    notes.add_note(text_without_com(message))
    bot.send_message(message.chat.id, 'Я добавил новую заметку и переместил вас в нее, хотите что-нибудь записать?')


@bot.message_handler(commands=['del', 'удалить'])
def remove_note(message):
    notes.remove_note(text_without_com(message))
    bot.send_message(message.chat.id, 'Я удалил эту заметку')


@bot.message_handler(commands=['list', 'список'])
def return_notes(message):
    bot.send_message(message.chat.id, f'Список заметок:\n{notes.return_notes()}')


@bot.message_handler(commands=['choose', 'выбрать'])
def choose_note(message):
    name_of_note, note = notes.choose_note(text_without_com(message))
    bot.send_message(message.chat.id, f'Заметка {name_of_note}:\n{note}')


@bot.message_handler(commands=['exit', 'ex', 'выйти'])
def exit_from_note(message):
    list_notes = notes.exit_from_note()
    bot.send_message(message.chat.id, f'Список заметок:\n{list_notes}')


@bot.message_handler(commands=['name', 'setname', 'имя'])
def change_name(message):
    notes.change_name(text_without_com(message))
    bot.send_message(message.chat.id, 'Имя измененно')


@bot.message_handler(commands=['add_s', 'добавить_с'])
def add_to_note(message):
    notes.add_to_note(text_without_com(message))
    bot.send_message(message.chat.id, 'Добавил запись')


@bot.message_handler(commands=['del_s', 'удалить_с'])
def remove_from_note(message):
    notes.remove_from_note(text_without_com(message))
    bot.send_message(message.chat.id, 'Все удалено')


@bot.message_handler(commands=['show', 'вывести'])
def output_note(message):
    name_of_note, note = notes.output_note(text_without_com(message))
    bot.send_message(message.chat.id, f'Заметка {name_of_note}:\n{note}')


bot.polling(none_stop=True)
