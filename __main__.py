import modules.bans
import modules.wiki
import modules.purge

import modules.version
import modules.changelog
import modules.pin
import modules.leavegroup
import modules.id
import modules.info 
import modules.sudo
import modules.warns
import os
from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters, run_async
from telegram import MessageEntity
import telegram.ext.dispatcher
import sys
from telegram import Message, Chat, Update, Bot, User



os.system("clear")
print("Initiating LoopedInfinity....")
print(" ")
print(" ")
start_message = """
Hello I am Loop. My full name is LoopedInfinity. Originally I was port of Marie but now I am brand new bot.(nothing from marie's code)
I was created by @yordanstoychev17 who is my maintainer.

If you want to ask a question or request a feature you can do that in @LoopedInfinity_group.

If you want to follow my development and get news about me you can easily do that if you follow @LoopedInfinity channel.

If you want to check everything about my options just type/click /help

If you want to donate to my creator you can type/click /donate

If you want to check out my repository(not uploaded yet): github.com/ysanatomic/TelegramManagementBot
"""

help_message = """

Bip Bip Loop here....

Available commands(in groups):
	/start
	/kick
	/ban
	/unban
	/kickme
	/wiki
	/donate
	/version
	/changelog


"""

donate_message = """

	If you want to donate to my creator (@yordanstoychev17) you can do it with paypal.
	
	paypal.me/YordanStoychev

"""







API = "HERE YOUR TOKEN" # API Token
OWNER_ID = 461490935 # Owner
OWNER_USERNAME = "yordanstoychev17" # my username

updater = Updater(token = API)
dispatcher = updater.dispatcher

def help(bot, update):
	if update.effective_chat.type == "private":
		bot.send_message(chat_id=update.message.chat_id, text = help_message)
	else:
		update.effective_message.reply_text("Type that on pm please!")

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

id_handler = CommandHandler('id', modules.id.id)
dispatcher.add_handler(id_handler)

version_handler = CommandHandler('version', modules.version.version)
dispatcher.add_handler(version_handler)

leaveit_handler = CommandHandler('leaveit', modules.leavegroup.leavegroup)
dispatcher.add_handler(leaveit_handler)

unpin_handler = CommandHandler('unpin', modules.pin.unpin)
dispatcher.add_handler(unpin_handler)

warn_handler = CommandHandler('warn', modules.warns.warn)
dispatcher.add_handler(warn_handler)


pin_handler = CommandHandler('pin', modules.pin.pin)
dispatcher.add_handler(pin_handler)

botshutdown_handler = CommandHandler('botshutdown', modules.sudo.disable)
dispatcher.add_handler(botshutdown_handler)

suspend_handler = CommandHandler('suspend', modules.sudo.suspend)
dispatcher.add_handler(suspend_handler)




#handlers:(import modules)


info_handler = CommandHandler('info', modules.info.info)
dispatcher.add_handler(info_handler)

kickme_handler = CommandHandler('kickme', modules.bans.kickme)
dispatcher.add_handler(kickme_handler)

ban_handler = CommandHandler('ban', modules.bans.ban)
dispatcher.add_handler(ban_handler)


unban_handler = CommandHandler('unban', modules.bans.unban)
dispatcher.add_handler(unban_handler)

changelog_handler = CommandHandler('changelog', modules.changelog.changelog)
dispatcher.add_handler(changelog_handler)


wiki_handler = CommandHandler('wiki', modules.wiki.wikisum)
dispatcher.add_handler(wiki_handler)



purge_handler = CommandHandler("purge", modules.purge.purge)
dispatcher.add_handler(purge_handler)

kick_handler = CommandHandler('kick', modules.bans.kick)
dispatcher.add_handler(kick_handler)



def start(bot, update):
	chat = update.effective_chat
	chatid = update.effective_chat.id
	user = update.effective_user
	userid = update.effective_user.id
	message = update.effective_message
	
	
	
	
	if update.effective_chat.type == "private":
		print(chatid)

		bot.send_message(chat_id=update.message.chat_id, text = start_message)
	else:
		if userid == OWNER_ID:
			print(chatid)
			print(chat)
			print(message)
			update.effective_message.reply_text("Hello Master of the Masters! My creator....")
		if userid != OWNER_ID:
			update.effective_message.reply_text("Hello my friend!")
		print(user)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
@run_async
def welcome(bot, update):
	chat = update.effective_chat
	user = update.effective_user
	nameofgroup = update.effective_message.chat.title
	userid = update.effective_user.id
	message = update.effective_message	
	all_members = update.effective_message.new_chat_members
	for newper in all_members:
		if newper.id == OWNER_ID:
			update.effective_message.reply_text("Ohh yea. The owner is here!")
		elif newper.id == bot.id:
			update.effective_message.reply_text("I AM HERE! Hello!")
		else:
			update.effective_message.reply_text("Hello " + update.effective_user.first_name + " to {}.".format(nameofgroup))
		
		
newmem_handler = MessageHandler(Filters.status_update.new_chat_members, welcome)
dispatcher.add_handler(newmem_handler)

def donate(bot, update):
	bot.send_message(chat_id=update.message.chat.id, text = donate_message)

donate_handler = CommandHandler('donate', donate)
dispatcher.add_handler(donate_handler)


updater.start_polling()
