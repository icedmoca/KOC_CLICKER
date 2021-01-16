from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import multiprocessing

def makeClickerInstance():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-web-security')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://kingoftheclicks.com/?ref=epicgamer')
        time.sleep(3)
        start = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[2]/div/div/div/footer/button[1]/span')
        start.click()
        time.sleep(1)
        removeButt = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span/span')
        global packetnum
        print("Starting clicks")
        while 1 == 1:
            for a in range(500):
                removeButt.click()
            time.sleep(1)
    except:
      pass

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=makeClickerInstance)
        p.start()
        time.sleep(5)
