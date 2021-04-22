from ..db import DBQuery
from ..settings import BOT_TOKEN, TB_AUTH_USERS
from telebot import TeleBot, logger
import logging

from .markup import *
from .str_messages import *

logger = logger
logger.setLevel(logging.INFO)

tb = TeleBot(BOT_TOKEN)

def dispatch_message(message):
    chat_ids = DBQuery.get_all_telegramm_chats()
    for chat_id in map(lambda el: el[0], chat_ids):
        tb.send_message(chat_id, message)

# common

@tb.message_handler(content_types=['text'], commands=['start'])
def start_command(message):
    DBQuery.save_telegramm_chat(message.chat.id)
    tb.send_message(message.from_user.id, msg_start())
    tb.send_message(message.from_user.id, msg_info())

@tb.message_handler(content_types=['text'], commands=['help'])
def info_command(message):
    tb.send_message(message.from_user.id, msg_info())
    

# auth

class User:
    def __init__(self, login):
        self.login = login
        self.password = None

auth_user_dict = {}

@tb.message_handler(content_types=['text'], commands=['auth'])
def auth_command(message):
    tb.send_message(message.from_user.id, msg_auth())
    tb.register_next_step_handler(message, process_auth_login)

def process_auth_login(message):
    auth_user_dict[message.chat.id] = User(message.text)
    tb.send_message(message.from_user.id, msg_auth_pswd())
    tb.register_next_step_handler(message, process_auth_pswd)

def process_auth_pswd(message):
    current_user = auth_user_dict[message.chat.id]
    current_user.password = message.text
    n_role = None
    for role, auth_parameters in TB_AUTH_USERS.items():
        if (auth_parameters['login'] == current_user.login and
            auth_parameters['password'] == current_user.password):
            n_role = role
            break
    
    if n_role != None:
        DBQuery.update_telegram_chat_role(message.chat.id, n_role)
        tb.send_message(message.from_user.id, msg_auth_succsess(n_role))
    else:
        tb.send_message(message.from_user.id, msg_auth_error())










# @tb.callback_query_handler(func=lambda call: call.message.text == "Yes/no?")
# def callback_query(call):
#     logger.info(call)
#     if call.data == "cb_yes":
#         tb.send_message(call.message.chat.id, "Answer is Yes")
#     elif call.data == "cb_no":
#         tb.send_message(call.message.chat.id, "Answer is No")
#     tb.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=None)

# @tb.message_handler(regexp="qwe")
# def message_handler(message):
#     tb.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())

# @tb.message_handler(func=lambda call: True)
# def test(message):
#     print('test')
#     tb.edit_message_reply_markup(message.chat.id, reply_markup=None)


# @tb.message_handler(regexp="SOME_REGEXP")
