from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters, run_async
from telegram import MessageEntity
import telegram.ext.dispatcher
import sys
from telegram import Message, Chat, Update, Bot, User

def pin(bot, update):
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
    messageid = messageid + 1
    
    if (isadmin == "creator") or (isadmin== "administrator") or (userid == 461490935):
        try:
            
            prev_message = message.reply_to_message
            prev_messagetext = message.reply_to_message.text
            bot.pinChatMessage(message.chat_id, message.reply_to_message.message_id)
            bot.delete_message(chat_id=message.chat_id,
                   message_id=messageid,
                    )
            print("----> pinned message in {}. The message is: {}".format(update.effective_chat.title, prev_messagetext))
            message.reply_text("Pinned!")
        except:
            message.reply_text("Please reply to message!")
    else: 
        message.reply_text("You are not an admin here!")
            

def unpin(bot, update):
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
    messageid = messageid + 1
    
    if (isadmin == "creator") or (isadmin== "administrator") or (userid == 461490935):
        try:
            
            bot.unpinChatMessage(message.chat_id, timeout=None)
            
            print("----> Unpinned message in {}".format(update.effective_chat.title,))
            message.reply_text("Unpinned!")
        except:
            message.reply_text("Error occured. Report it to @LoopedInfinity_group")
    else: 
        message.reply_text("You are not an admin here!")