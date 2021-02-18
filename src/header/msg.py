import sys
import telegram

class TelegramBotManager:
    def sendmsg(self, botToken, chatID, sendMsg):
        try:
            AlaramBot = telegram.Bot(botToken)
            AlaramBot.sendMessage(chatID, sendMsg)
        except:
             sys.exit()