from telebot import types


def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_off = types.KeyboardButton("shutdown")
    btn_hibernate = types.KeyboardButton("hibernate")
    btn_sound = types.KeyboardButton("sound")
    markup.add(btn_sound, btn_hibernate, btn_off)
    return markup


def sound_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_undo = types.KeyboardButton("menu")
    btn_mute = types.KeyboardButton("mute")
    btn_up = types.KeyboardButton("+10 vol")
    btn_down = types.KeyboardButton("-10 vol")
    btn_prevtrack = types.KeyboardButton("prevtrack")
    btn_playpause = types.KeyboardButton("playpause")
    btn_nexttrack = types.KeyboardButton("nexttrack")
    markup.add(btn_mute, btn_up, btn_down, btn_prevtrack, btn_playpause, btn_nexttrack, btn_undo)
    return markup


