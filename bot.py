from telegram.ext import Updater,MessageHandler,Filters
from telegram import Bot,Update

botUpdater = Updater(token="token from @botfather")
botDispatcher = botUpdater.dispatcher


def sticker_recived(bot: Bot, update: Update):
    admins = [admin.user.id for admin in bot.get_chat_administrators(chat_id=update.message.chat_id)]
    if update.message.from_user.id not in admins:
        bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id, timeout=0)


stickerRecivedHandeler = MessageHandler(Filters.sticker, sticker_recived)
botDispatcher.add_handler(stickerRecivedHandeler)
botUpdater.start_polling()
botUpdater.idle()
