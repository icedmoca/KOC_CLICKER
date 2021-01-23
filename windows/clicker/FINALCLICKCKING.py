from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
def makeClickerInstance():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r'chromedriver/chromedriver.exe', options=chrome_options)
    driver.get("https://kingoftheclicks.com/?ref=zodicalpeak")
    time.sleep(3)
    start = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[2]/div/div/div/footer/button[1]/span')
    start.click()
    time.sleep(1)
    removeButt = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span/span')
    x = 0
    progress = 0
    print('STARTING')
    while x < 10000:
        removeButt.click()
        time.sleep(0.01)
        x = x + 1
        if (x % 1) == 0:
            progress = progress + 1
            print(str(progress) + "CLICKS PREFORMED")
    driver.quit()

while 1 == 1:
    makeClickerInstance()
    print('RESTARTING')
