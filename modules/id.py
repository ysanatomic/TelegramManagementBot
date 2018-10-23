from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters, run_async
import telegram.ext.dispatcher
import sys
from telegram import Message, Chat, Update, Bot, User


def id(bot, update):
    
    chatid = update.effective_chat.id
    
    userid = update.effective_user.id
    message = update.effective_message
    
    messagetext = update.effective_message.text
    status = bot.get_chat_member(chatid, userid)
    
    messagetext = messagetext[4:]

    message.reply_text("Your id is {}.".format(update.effective_user.id))
    print("---> {} id is {}".format(update.effective_user.username, update.effective_user.id))
