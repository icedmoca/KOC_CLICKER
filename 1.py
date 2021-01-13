import multiprocessing
import time
from selenium import webdriver

def makeClickerInstance():
    try:
        #driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors.
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://kingoftheclicks.com/?ref=zodicalpeak")
        time.sleep(3)
        start = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[2]/div/div/div/footer/button[1]/span')
        start.click()
        time.sleep(1)
        removeButt = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span/span')
        x = 0
        print("STARTING CLICK LOOP")
        while x < 10000:
            removeButt.click()
            time.sleep(0.01)
            x = x + 1
    except:
        print("Error Starting")
    driver.quit()


if __name__ == '__main__':
  for i in range(15):
    p = multiprocessing.Process(target=makeClickerInstance)
    p.start()
