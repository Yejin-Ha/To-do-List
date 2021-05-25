
import datetime
def getTime():        
    now = datetime.datetime.now()
    nowTime =  now.strftime('%y-%m-%d %H:%M')
    return nowTime
