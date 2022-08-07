import logging
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
logging.basicConfig(level=logging.INFO)
load_dotenv()
SLACK_BOT_TOKEN = os.environ["Atomic_bot_Socket_Mode_Token"]
SLACK_APP_TOKEN = os.environ["Atomic_bot_User_OAuth_Token"]

atomic = App(token= SLACK_BOT_TOKEN)

@atomic.event("app_mention")
def mention_handler(body, context,payload,options, say, event):
    say("Hello World!")

@atomic.event("message")
def message_handler(body, context, payload, options, say, event):
    pass

if__name__=="__main__":
handler=SocketModeHandler(atomic, SLACK_APP_TOKEN)
handler.start()


