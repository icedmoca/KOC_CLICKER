from selenium import webdriver
import time
def makeClickerInstance():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://kingoftheclicks.com/?ref=epicgamer")
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
    driver.quit()

while 1 == 1:
    makeClickerInstance()
    print("RESTARTING")
