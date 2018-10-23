from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters, run_async
from telegram import MessageEntity
import telegram.ext.dispatcher
import sys
from telegram import Message, Chat, Update, Bot, User

versionbot = "0.5"

def version(bot, update):
    update.effective_message.reply_text("Version: {}".format(versionbot))