import requests
from datetime import datetime, timedelta
from security import *
import schedule
import time




def send_message_slack(text):
    while True:
        requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+slack_token},
            data={"channel": slack_location, "text": text})


#  seconds, minutes, hours, days, weeks

# 매일 7시 30분 45초 실행
schedule.every().day.at("07:30:45").do(send_message_slack, "매일 7시 30분 45초 에 실행" + str(datetime.now()))
# 10초에 한번씩 실행
schedule.every(10).second.do(send_message_slack, "10초에 한번씩 실행" + str(datetime.now()))
# 10분에 한번씩 실행
schedule.every(10).minutes.do(send_message_slack, "10분에 한번씩 실행" + str(datetime.now()))
# 매 시간 실행
schedule.every().hour.do(send_message_slack, "매 시간 실행" + str(datetime.now()))
# 매일 10:30 에 실행
schedule.every().day.at("10:30").do(send_message_slack, "매일 10:30 에 실행" + str(datetime.now()))
# 매주 월요일 실행
schedule.every().monday.do(send_message_slack, "매주 월요일 실행" + str(datetime.now()))
# 매주 수요일 13:15 에 실행
schedule.every().wednesday.at("13:15").do(send_message_slack, "매주 수요일 13:15 에 실행" + str(datetime.now()))
# 매분 23초에 실행
schedule.every().minute.at(":23").do(send_message_slack, "매분 23초에 실행" + str(datetime.now()))
# 매시간 42분에 실행
schedule.every().hour.at(":42").do(send_message_slack, "매시간 42분에 실행" + str(datetime.now()))
# 5시간 20분 30초마다 작업 실행
schedule.every(5).hours.at("20:30").do(send_message_slack, "5시간 20분 30초마다 작업 실행" + str(datetime.now()))

# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(send_message_slack, "시작 후 5분에서 10분사이에 작동" + str(datetime.now()))



while True:
    schedule.run_pending()
    time.sleep(1)