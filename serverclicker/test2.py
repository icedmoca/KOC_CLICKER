from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import multiprocessing

def make_clicker_instance():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-web-security')
        
        driver = webdriver.Chrome(options=chrome_options)
        status = 0
        
        while status == 0:
            try:
                driver.get('https://kingoftheclicks.com/?ref=epicgamer')
                time.sleep(3)
                start_button = driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/main/div[3]/div[2]/div/div/div/footer/button[1]/span'
                )
                start_button.click()
                status = 1
            except Exception as e:
                print(f"Error in initial navigation and click: {e}")
                time.sleep(1)
        
        time.sleep(1)
        remove_button = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span/span'
        )
        
        while True:
            try:
                remove_button.click()
                time.sleep(0.01)
            except Exception as e:
                print(f"Error clicking remove button: {e}")
                time.sleep(1)
    except Exception as e:
        print(f"Error in make_clicker_instance: {e}")
    finally:
        try:
            driver.quit()
        except Exception as e:
            print(f"Error quitting driver: {e}")

if __name__ == '__main__':
    processes = []
    for _ in range(12):
        p = multiprocessing.Process(target=make_clicker_instance)
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
