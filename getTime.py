
import datetime # datetime module import

def getTime():        
    now = datetime.datetime.now()
    nowTime =  now.strftime('%y-%m-%d %H:%M')
    return nowTime
