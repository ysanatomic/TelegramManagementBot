from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters, run_async
import telegram.ext.dispatcher
import sys
from telegram import Message, Chat, Update, Bot, User



def purge(bot, update):
    
    chat = update.effective_chat
    chatid = update.effective_chat.id
    user = update.effective_user
    userid = update.effective_user.id
    message = update.effective_message
    messageid = message.message_id
    messagetext = update.effective_message.text
    status = bot.get_chat_member(chatid, userid)
    isadmin = status.status
    i = 0
    messagetext = messagetext[7:]
    messageint = int(messagetext)
    if (isadmin == "creator") or (isadmin== "administrator") or (userid == 461490935):
        
        try:
            while i<=messageint: 
                
                bot.delete_message(chat_id=message.chat_id,
                        message_id=messageid,
                            )
                messageid = messageid - 1
                i += 1
                
                
            print("---> "+update.effective_chat.title + " ----> purged {} messages".format(i))
        except:
            message.reply_text("Something went wrong with this group purge!")
    else: 
        message.reply_text("You are not an admin here!")

    

