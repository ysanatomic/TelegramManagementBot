from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters, run_async
from telegram import MessageEntity
import telegram.ext.dispatcher
import sys
from telegram import Message, Chat, Update, Bot, User
import time
import os
import signal

def disable(bot, update):
    chat = update.effective_chat
    chatid = update.effective_chat.id
    user = update.effective_user
    nameofgroup = update.effective_message.chat.title
    userid = update.effective_user.id
    message = update.effective_message
    messagetext = update.effective_message.text
    all_members = update.effective_message.new_chat_members
    messageid = message.message_id
    status = bot.get_chat_member(chatid, userid)
    isadmin = status.status

    if userid==461490935:
        message.reply_text("Okay. Initiating shutdown...")
        print("")
        print("SHUTDOWNED BY THE OWNER")
        print("")
        os.kill(os.getppid(), signal.SIGHUP)
    else:
        message.reply_text("Only @yordanstoychev17 can execute that command!")



def suspend(bot, update):
    chat = update.effective_chat
    chatid = update.effective_chat.id
    user = update.effective_user
    nameofgroup = update.effective_message.chat.title
    userid = update.effective_user.id
    message = update.effective_message
    messagetext = update.effective_message.text
    all_members = update.effective_message.new_chat_members
    messageid = message.message_id
    status = bot.get_chat_member(chatid, userid)
    isadmin = status.status
    seconds = messagetext[9:]
    seconds = int(seconds)
    if userid==461490935:
        
        message.reply_text("I am disabled for {} seconds!".format(seconds))
        print("")
        print("SUSPENDED BY THE OWNER")
        print("")
        time.sleep(seconds)
        message.reply_text("I am back again!")
        print("")
        print("THE BOT IS BACK ON")
        print("")
    else:
        message.reply_text("Only @yordanstoychev17 can execute that command!")