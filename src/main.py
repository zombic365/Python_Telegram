import sys
from header.time import *
from header.msg import TelegramBotManager as telegram
from header.json_conf import JsonManager
jsonconf = JsonManager('Json 파일 경로')

def sysExit():
    sys.exit()

if __name__ == "__main__":
    
    check_day = getNow('day_type1')
    check_time = getNow('time_type2')

    bottoken = jsonconf.values.Telegram.bot_token
    chatid = jsonconf.values.Telegram.chat_id

    if check_day == "01":
        getFamilyday()
    else:
        check_family_day = jsonconf.values.Schedule.familyday
        if str(check_family_day) == check_day:
            if check_time == "09:00":
                telegram.sendmsg(telegram, bottoken, chatid, '근무 시작입니다.\n오늘은 가정의 날이니 5시 퇴근입니다.\n하루도 화이팅 하세요!')
            elif check_time == "11:10":
                telegram.sendmsg(telegram, bottoken, chatid, '오전 11시가 넘었습니다.\n커피 마시고 오세요!')
            elif check_time == "12:30":
                telegram.sendmsg(telegram, bottoken, chatid, '점심시간입니다.\n식사 맛있게 하세요~')
            elif check_time == "17:00":
                telegram.sendmsg(telegram, bottoken, chatid, '가정의 날로 5시 퇴근 입니다.\n오늘 하루도 고생하셨습니다.')
        else:
            if check_time == "09:00":
                telegram.sendmsg(telegram, bottoken, chatid, '근무 시작입니다.\n오늘 하루도 화이팅 하세요!')
            elif check_time == "11:10":
                telegram.sendmsg(telegram, bottoken, chatid, '오전 11시가 넘었습니다.\n커피 마시고 오세요!')
            elif check_time == "12:30":
                telegram.sendmsg(telegram, bottoken, chatid, '점심시간입니다.\n식사 맛있게 하세요~')
            elif check_time == "17:00":
                telegram.sendmsg(telegram, bottoken, chatid, '퇴근 입니다.\n오늘 하루도 고생하셨습니다.')
            elif check_time == "18:00":
                telegram.sendmsg(telegram, bottoken, chatid, '퇴근 입니다.\n오늘 하루도 고생하셨습니다.')