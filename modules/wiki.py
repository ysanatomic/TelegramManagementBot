from telegram.ext import CommandHandler, Updater
from telegram import Message, Chat, Update, Bot, User
import telegram.ext.dispatcher
from telegram.ext import MessageHandler, Filters, run_async

import wikipedia

def wikisum(bot, update):
    chat = update.effective_chat
    chatid = update.effective_chat.id
    user = update.effective_user
    userid = update.effective_user.id
    message = update.effective_message
    messagetext = update.effective_message.text
    try:
        
        
        forsum = messagetext[6:]
        if forsum == "":
            message.reply_text("Right usage: /wiki <phrase for search>")
        else:
            sum = wikipedia.summary(forsum)
            sumz = sum[:500]

            message.reply_text(sumz)
            print("---> Wikipedia Summary was runned in {}. The summary was: {}".format(update.effective_chat.title, forsum))

    except:
        bot.send_message(chat_id=update.message.chat.id, text="Sorry the wiki summary failed.")

