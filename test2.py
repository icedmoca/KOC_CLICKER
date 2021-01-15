from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
from random import randint
import multiprocessing
packetnum = False

def interceptor(request):
    try:
        global packetnum
        if request.method == 'POST' and request.headers['Content-Type'] == 'application/json;charset=UTF-8' and request.headers['Host'] == 'gobo66g2oj.execute-api.us-east-1.amazonaws.com':
            body = request.body.decode('utf-8')
            if '"number":' in body:
                try:
                    newnum = str(randint(2,5))
                    body = body.replace('"number":', ('"number":' + newnum))
                    request.body = body.encode('utf-8')
                    del request.headers['Content-Length']
                    request.headers['Content-Length'] = str(len(request.body))
                    packetnum = True
                except:
                    pass
    except:
        pass
def makeClickerInstance():
    try:
        print("Initilizing Instance")
        options = {
            'backend': 'mitmproxy'
        }
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-web-security')
        driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)
        driver.get('https://kingoftheclicks.com/?ref=zodicalpeak')
        time.sleep(6)
        start = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[2]/div/div/div/footer/button[1]/span')
        start.click()
        time.sleep(1)
        removeButt = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span/span')
        global packetnum
        print("Starting clicks")
        for x in range(10000000000):
            packetnum = False
            driver.request_interceptor = interceptor
            for a in range(500):
                removeButt.click()
            while packetnum == False:
                try:
                    interceptor(driver.last_request)
                except:
                    pass
        driver.quit()
    except:
        print("DriverCrashed restarting...")
        try:
            driver.quit()
        except:
            pass

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=makeClickerInstance)
        p.start()
