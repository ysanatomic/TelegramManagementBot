from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters, run_async
from telegram import MessageEntity
import telegram.ext.dispatcher
import sys
from telegram import Message, Chat, Update, Bot, User


def warn(bot, update):
    chat = update.effective_chat
    chatid = update.effective_chat.id
    user = update.effective_user
    userid = update.effective_user.id
    message = update.effective_message
    messagetext = update.effective_message.text
    status = bot.get_chat_member(chatid, userid)
    isadmin = status.status
    if (isadmin == "creator") or (isadmin== "administrator") or (userid == 461490935):
        try:
            messagetext = messagetext[6:]
            prev_message = message.reply_to_message
            prev_messagetext = message.reply_to_message.text
            prev_message.reply_text("""Warned by @{}.

Reason For Warn:
{}
    """.format(update.effective_user.username, messagetext))
        except:
            message.reply_text("Please, reply on message!")
    else:
        message.reply_text("You're not an admin!")