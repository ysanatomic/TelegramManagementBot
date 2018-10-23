from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters, run_async
from telegram import MessageEntity
import telegram.ext.dispatcher
import sys
from telegram import Message, Chat, Update, Bot, User
changelogtext = """
ChangeLog for version 0.5:
    Fixed things:
    -/ban
    -/kick
    -/unban
    Updated commands:
    -/version command
    -/changelog command
    -/wiki command
    -/ban
    -/kick
    -/unban
    -/pin
    -/purge <number>
    -/id
    
    Added commands:
    -/info
    -/id
    
"""
def changelog(bot, update):
    update.effective_message.reply_text(changelogtext)