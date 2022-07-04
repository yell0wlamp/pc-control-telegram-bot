import telebot
import os
import pyautogui as pag

import info
import handler

bot = telebot.TeleBot(info.bot_token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "main menu", reply_markup=handler.main_menu())



@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.from_user.id == info.admin_id:  # verification
        # main menu
        if message.text == "shutdown":
            os.system("shutdown /s /t 1")
        elif message.text == "hibernate":
            os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')
        # sound menu
        elif message.text == "sound":
            bot.send_message(message.chat.id, "sound setting", reply_markup=handler.sound_menu())
        elif message.text == "menu":
            start(message)
        elif message.text == "mute":
            pag.press('volumemute', presses=1)
        elif message.text == "+10 vol":
            pag.press('volumeup', presses=5)
        elif message.text == "-10 vol":
            pag.press('volumedown', presses=5)
        elif message.text == "prevtrack":
            pag.press('prevtrack')
        elif message.text == "playpause":
            pag.press('playpause')
        elif message.text == "nexttrack":
            pag.press('nexttrack')
    else:
        bot.send_message(message.chat.id, "you're not an admin")


bot.polling(none_stop=True)
