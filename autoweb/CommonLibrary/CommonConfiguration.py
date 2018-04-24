from datetime import datetime
import os

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
DRIVER_PATH = os.path.join(BASE_PATH, 'driver')
Upload_PATH = os.path.join(BASE_PATH, 'Upload')
TestCases_PATH = os.path.join(BASE_PATH, 'suite')

def baseUrl():
    # return "https://pan.baidu.com/"
    return "http://sahitest.com/demo/index.htm"
    # return "https://www.baidu.com"

#change time to str

def getCurrentTime():
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format)

# Get time diff
def timeDiff(starttime,endtime):
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.strptime(endtime,format) - datetime.strptime(starttime,format)