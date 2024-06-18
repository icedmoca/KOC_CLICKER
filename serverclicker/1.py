import time
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from random import randint
import multiprocessing

packetnum = False

def interceptor(request):
    global packetnum
    try:
        if request.method == 'POST' and request.headers.get('Content-Type') == 'application/json;charset=UTF-8' and \
                request.headers.get('Host') == 'gobo66g2oj.execute-api.us-east-1.amazonaws.com':
            body = request.body.decode('utf-8')
            if '"number":' in body:
                newnum = str(randint(170, 180))
                body = body.replace('"number":', f'"number":{newnum}')
                request.body = body.encode('utf-8')
                request.headers['Content-Length'] = str(len(request.body))
                packetnum = True
    except Exception as e:
        print(f"Error in interceptor: {e}")

def make_clicker_instance():
    global packetnum
    try:
        print("Initializing Instance")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-web-security')

        seleniumwire_options = {'backend': 'mitmproxy'}
        driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options, options=chrome_options)
        driver.request_interceptor = interceptor
        driver.get('https://kingoftheclicks.com/?ref=zodicalpeak')
        time.sleep(6)

        start_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[2]/div/div/div/footer/button[1]/span')
        start_button.click()
        time.sleep(1)
        click_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span/span')

        print("Starting clicks")
        while True:
            packetnum = False
            for _ in range(500):  # Number of clicks at a time
                click_button.click()
            while not packetnum:
                time.sleep(0.1)
    except Exception as e:
        print(f"Driver crashed: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == '__main__':
    processes = []
    for _ in range(10):  # Number of instances to run
        p = multiprocessing.Process(target=make_clicker_instance)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
