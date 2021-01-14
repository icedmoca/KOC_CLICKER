from selenium import webdriver
import time
def makeClickerInstance():
    global driver
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://kingoftheclicks.com/?ref=zodicalpeak")
        time.sleep(2)
        start = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[2]/div/div/div/footer/button[1]/span')
        start.click()
        time.sleep(1)
        removeButt = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span/span')
        print("STARTING CLICK LOOP")
        for x in range(10000):
            removeButt.click()
            time.sleep(0.01)
    except:
        print("DRIVER FAILED TO START. RESTARTING....")
    try:
        driver.quit()
    except:
        pass

while 1 == 1:
    makeClickerInstance()
    print("RESTARTING")
