@run_async

def dark(bot: Bot, update: Update):

    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages

    message = update.effective_message

    if message.reply_to_message:

      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))

    else:

      message.reply_text(random.choice(SFW_STRINGS))
