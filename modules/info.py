from telegram.ext import CommandHandler, Updater
from telegram import Message, Chat, Update, Bot, User
import telegram.ext.dispatcher

def info(bot, update):
    chat = update.effective_chat
    chatid = update.effective_chat.id
    user = update.effective_user
    userid = update.effective_user.id
    message = update.effective_message
    status = bot.get_chat_member(chatid, userid)
    isadmin = status.status
    something = bot.get_chat_member(chatid, userid)
    try:
        prev_message = message.reply_to_message
        prev_user_fn = prev_message.from_user.first_name
        prev_user_sc = prev_message.from_user.last_name
        prev_user_id = prev_message.from_user.id
        prev_user_username = prev_message.from_user.username
        user_id = prev_message.from_user.id
        
        message.reply_text("""
User information:
First name: {}
Last name: {}
Username: @{}

ID: {}


        
        
        """.format(prev_user_fn, prev_user_sc, prev_user_username, prev_user_id))

    except:
        message.reply_text("""
User information:
First name: {}
Last name: {}
Username: @{}

ID: {}


        
        
        """.format(update.effective_user.first_name, update.effective_user.last_name, update.effective_user.username, user.id))