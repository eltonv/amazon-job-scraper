from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

divider = '-----------------------------------'
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://hiring.amazon.com/app#/jobSearch")
driver.implicitly_wait(30)

#Click consent to the prompt that automatically shows up
consentButton = driver.find_element("css selector", 'button.e4s17lp0.css-1jwvbdk')
consentButton.click()
driver.implicitly_wait(10)

# Select search box to enter desired city
city = driver.find_element("css selector", 'input#zipcode-nav-guide.css-gz5rcq')
city.click()
driver.implicitly_wait(5)
city.send_keys('san bernardino')
driver.implicitly_wait(10)

#Select the first city that pops up (usually the correct one)
selector = driver.find_element("css selector", 'li#zipcode-nav-guide-item-0.css-1qff820')
selector.click()
time.sleep(10)

jobs = driver.find_elements("css selector", 'div.pointer.focusableItem.stencil-2021.jobCardItem.css-1z8p01')

#check if theres no jobs(nojob css selector)
if len(jobs) > 0:

    for job in jobs:
        listings = job.get_attribute('innerText').splitlines()
        if 'Bonus' in listings[0]:
            if 'Part Time' in listings[3]:
                print(listings[3])
                print(divider)
        else:
            if 'Part Time' in listings[3]:
                print(listings[2])
                print(divider)
else:
    print('No jobs found')


#previous_height = driver.execute_script('return document.body.scrollHeight')
#while True:
#    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
#    time.sleep(5)
#    new_height = driver.execute_script('return document.body.scrollHeight')
#    if new_height == previous_height:
#        break
 #   previous_height = new_height