
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import multiprocessing
from fake_useragent import UserAgent
def makeClickerInstance():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('user-agent=' + UserAgent(cache=False).chrome)
        driver = webdriver.Chrome(options=chrome_options, executable_path=r'../../../Desktop/KINGCLICKER/chromedriver/chromedriver.exe')
        status = 0
        while status == 0:
            try:
                driver.get('https://kingoftheclicks.com/?ref=zodicalpeak')
                time.sleep(3)
                start = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[2]/div/div/div/footer/button[1]/span')
                start.click()
                print('worked')
                status = status + 1
            except:
                print('trying again')
                pass
        time.sleep(1)
        removeButt = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span/span')
        print("Starting clicks")
        while 1 == 1:
            removeButt.click()
            time.sleep(0.01)
    except:
      pass
if __name__ == '__main__':
    for i in range(1):
        p = multiprocessing.Process(target=makeClickerInstance)
        p.start()
