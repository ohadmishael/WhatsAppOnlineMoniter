#whatsapp online follower and printer
from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import gmtime, strftime, sleep

#Enter TARGET (person you would like to moniter) and TIMETORUN(time to run the project in seconds)
TARGET = 'italynum'
TIMETORUN = 100

###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
def check_exists_by_class_name(classname):
    try:
        browser.find_element_by_class_name(classname)
    except NoSuchElementException:
        return False
    return True
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')
browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com')
while 1 is 1:
    print ()
    print('\nYou got 15 seconds to visit the website and scan the QR code.')
    print('Waiting QR Scanning...')
    sleep(15)
    try:
        if (check_exists_by_xpath('//*[@title="Search or start new chat"]') is True):
            SCANNED = True
            #print('Success!')
    except NoSuchElementException:
        pass
        
search = browser.find_element_by_class_name('eiCXe')
search.send_keys(TARGET)
sleep(2)
x = "//*[contains(text(), '"
y = "')]"
TARGET = str(TARGET)
send  = x + TARGET +y
send = str(send)
browser.find_element_by_xpath(send).click()
time = 0
print ()
print ()
print ()
print ()
print ()
print ()
print ('Showing Activity in whatsapp of: ' + TARGET)
for i in range(TIMETORUN):
    if (check_exists_by_xpath('//*[@title="online"]') is True or (check_exists_by_xpath('//*[@title="typing..."]') is True)):
        #print ('online')
        if time is 0:
            print ('Logged in: '+ str(datetime.now().strftime('%H:%M:%S')))

        time = datetime.now().strftime('%H:%M:%S')
    if time is not 0:
        x = time
        y = datetime.now().strftime('%H:%M:%S')
        t1, t2 = pd.to_datetime(x), pd.to_datetime(y)
        if (pd.Timedelta(t2 - t1).seconds > 1.1):
            print ('Logged Out: ' + str(datetime.now().strftime('%H:%M:%S')))
            time = 0
    sleep(1)
