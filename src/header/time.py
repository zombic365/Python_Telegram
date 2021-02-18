import json, sys
from datetime import datetime
from .json_conf import JsonManager
jsonconf = JsonManager('Json 파일 경로')

now = datetime.now()
year = now.year
month = now.month

def getNow(selectArg):
    if 'day_type1' in selectArg:
        Result = now.strftime("%d")    
    elif 'day_type2' in selectArg:
        Result = now.strftime("%m-%d")    
    elif 'time_type1' in selectArg:
        Result = now.strftime("%H")
    elif 'time_type2' in selectArg:
        Result = now.strftime("%H:%M") 
    return Result

def getFamilyday():
    Days = []
    if (year%4) == 0 and (year%100) != 0 or (year%400) == 0:
        Days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        Days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    i = None
    cnt = 0
    for i in range(1, Days[month]+1):
        weekday = datetime(year,month,i).weekday() #### 달의 첫번째 월요일이 첫째주 월요일
        if weekday == 0:
            cnt = cnt + 1
            if cnt == 3:
                # familyday = i
                jsonconf.update({'Schedule': {'familyday': i+2}})
                sys.exit()