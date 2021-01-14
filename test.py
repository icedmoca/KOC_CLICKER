from seleniumwire import webdriver  # Import from seleniumwire
import time
# Create a new instance of the Firefox driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://kingoftheclicks.com/?ref=epicgamer')

def interceptor(request):
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        # The body is in bytes so convert to a string
        print('starting injection')
        body = request.body.decode('utf-8')
        # Load the JSON
        data = json.loads(body)
        # Add a new property
        print(data)
        #data[2] = '"number":200'
        # Set the JSON back on the request
        request.body = json.dumps(data).encode('utf-8')
        # Update the content length
        del request.headers['Content-Length']
        request.headers['Content-Length'] = str(len(request.body))

# Access requests via the `requests` attribute
time.sleep(6)
start = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[2]/div/div/div/footer/button[1]/span')
start.click()
time.sleep(1)
print('STARTING')
removeButt = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span/span')
driver.request_interceptor = interceptor

        #for x in range(1):
removeButt.click()
pRequest = driver.wait_for_request('https://gobo66g2oj.execute-api.us-east-1.amazonaws.com/dev/modify', timeout=10)
try:
    interceptor(pRequest)
except:
    print('didnt work lol get good')
    pass
