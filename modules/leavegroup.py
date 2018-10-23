from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters, run_async
from telegram import MessageEntity
import telegram.ext.dispatcher
import sys
from telegram import Message, Chat, Update, Bot, User

ownerid = 461490935

def leavegroup(bot, update):
    chat = update.effective_chat  
    chatid = update.effective_chat.id
    user = update.effective_user  
    userid = update.effective_user.id
    message = update.effective_message
    status = bot.get_chat_member(chatid, userid)
    isadmin = status.status
    if userid == ownerid:
        message.reply_text("The owner told me to leave so I have to leave now. Bye!")
        bot.leave_chat(update.message.chat.id)
    else:
        pass
