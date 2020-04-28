from ChatBot import Telegram_Bot
from WeirdTalk import weirdTalk
import emoji

bot = Telegram_Bot("config.cfg")

def makeReply(msg):
    if msg == "/start":
        reply = "Welcome to Weird Talk Bot \N{robot face} \nStart by sending me a message!"
        print(user + ": " + msg)
        return reply
    elif msg is not None:
        reply = weirdTalk(msg)
        print(user + ": " + msg)
        return reply

update_id = None

while True:
    print("...")
    updates = bot.getUpdates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None

            try:
                sticker = item["message"]["sticker"]
            except:
                sticker = None

            if sticker is not None:
                message = "Sorry I cannot compute this."

            from_ = item["message"]["from"]["id"]
            user = item["message"]["from"]["first_name"]
            reply = makeReply(message)
            bot.sendMessage(reply, from_)