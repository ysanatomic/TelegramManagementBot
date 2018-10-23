from telegram.ext import CommandHandler, Updater
from telegram import Message, Chat, Update, Bot, User
import telegram.ext.dispatcher


def kickme(bot,update):
	chat = update.effective_chat  
	chatid = update.effective_chat.id
	user = update.effective_user 
	userid = update.effective_user.id
	message = update.effective_message
	if update.effective_chat.type == "private":
		bot.send_message(update.message.chat_id, "Bip Bip.... Try that in group please...")
	else:

		try:

			res = chat.unban_member(userid)
			message.reply_text("I kicked you!")


		except:
			message.reply_text("That command is not Available for you! Sorry.")



def kick(bot, update):
	chat = update.effective_chat  
	chatid = update.effective_chat.id
	user = update.effective_user  
	userid = update.effective_user.id
	message = update.effective_message
	status = bot.get_chat_member(chatid, userid)
	isadmin = status.status
	messagetext = update.effective_message.text
	usertokick = messagetext[7:]
	
	if update.effective_chat.type == "private":
		bot.send_message(update.message.chat_id, "Bip Bip.... Try that in group please...")
	else:

		if (isadmin == "creator") or (isadmin == "administrator") or (userid == 461490935):
			something = bot.get_chat_member(chatid, userid)
			print(something)
			prev_message = message.reply_to_message
			user_id = prev_message.from_user.id
			print(prev_message.from_user)
			if usertokick == "":
				if user_id == bot.id:
					message.reply_text("Srlsy?")

				elif prev_message.from_user.id == userid:
					message.reply_text("You want to kick yourself?(if the answer is yes just use /kickme)")

				elif user_id != bot.id:
					try:
						res = chat.unban_member(user_id)
						message.reply_text("Wow. I just kicked that guy!")


					except:
						message.reply_text("Something went wrong!")
				elif userid == 461490935:
					message.reply_text("That is my creator. He can't be kicked!")

		elif isadmin =="member":
			message.reply_text("Man... You are not even an admin....")
		else:
			something = bot.get_chat_member(chatid, userid)
			print(something)
			message.reply_text("Error. Please fix me @yordanstoychev17")


def unban(bot, update):
	
	chat = update.effective_chat  
	chatid = update.effective_chat.id
	user = update.effective_user  
	userid = update.effective_user.id
	message = update.effective_message
	status = bot.get_chat_member(chatid, userid)
	isadmin = status.status

	if update.effective_chat.type == "private":
		bot.send_message(update.message.chat_id, "Bip Bip.... Try that in group please...")
	else:

		if (isadmin == "creator") or (isadmin == "administrator") or (userid == 461490935):
			try:
				prev_message = message.reply_to_message
				user_id = prev_message.from_user.id
				chat.unban_member(user_id)
				message.reply_text("That user was unbanned!")
			except:
				message.reply_text("Something went wrong!")

		elif isadmin == "member":
			message.reply_text("Man... You are not even an admin....")
		else:
			message.reply_text("Error. Please fix me @yordanstoychev17")



def ban(bot, update):
	
	chat = update.effective_chat  
	chatid = update.effective_chat.id
	user = update.effective_user  
	userid = update.effective_user.id
	message = update.effective_message
	status = bot.get_chat_member(chatid, userid)
	isadmin = status.status
	if update.effective_chat.type == "private":
		bot.send_message(update.message.chat_id, "Bip Bip.... Try that in group please...")
	else:
		if (isadmin == "creator") or (isadmin == "administrator") or (userid == 461490935):
			something = bot.get_chat_member(chatid, userid)
			print(something)
			prev_message = message.reply_to_message
			user_id = prev_message.from_user.id
			print(prev_message.from_user)
			if user_id == bot.id:
				message.reply_text("Srlsy?")

			elif prev_message.from_user.id == userid:
				message.reply_text("You want to ban yourself?")

			elif user_id != bot.id:
				try:
					res = chat.kick_member(user_id)
					message.reply_text("Wow. I just banned that guy!")

				except:
					message.reply_text("Something went wrong!")
			elif userid == 461490935:
				message.reply_text("That is my creator. He can't be banned!")

		elif isadmin == "member":
			message.reply_text("Man... You are not even an admin....")
		else:
			message.reply_text("Error. Please fix me @yordanstoychev17")

	
