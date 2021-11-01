import requests
from datetime import datetime, timedelta
from security import *




def send_message_slack(text):
    requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+slack_token},
        data={"channel": slack_location, "text": text})

send_message_slack("안녕하세요" + str(datetime.now()))