from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

'''
#To disable notifications, cookies, geolocation, infobars
from selenium.webdriver.chrome.options import Options 
options = Options()
prefs = {
    "profile.default_content_setting_values.cookies": 2,
    "profile.block_third_party_cookies": True,
    "profile.default_content_setting_values.notifications": 2
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-notifications")
options.add_argument("--disable-geolocation")
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=options)
'''

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(3)

#Navigation commands to move backward & forward
driver.get("https://www.youtube.com/VamsiBhavani")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)

#To fill forms automatically
driver.get('https://freeonlinenotepad.net/')
driver.find_element(By.ID, 'notepad').send_keys("hello...")
driver.find_element(By.XPATH, '//*[@id="notepad"]').send_keys("hello ganeshhhhhh...")
time.sleep(3)

#Click option same for radio & check box
driver.get('https://www.w3schools.com/html/html_form_input_types.asp')
time.sleep(9)
driver.find_element(By.XPATH, '//*[@id="css"]').click()
time.sleep(3)

#To get all links from the page. 
driver.get('https://www.youtube.com/@manikanta.t9940')
links = driver.find_elements(By.TAG_NAME, "a")
for i in links:
    print(i.text)

#Alerts & popups
driver.get('https://testautomationpractice.blogspot.com/')
driver.find_element(By.XPATH, '//*[@id="promptBtn"]').click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="promptBtn"]').click()
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(3)

#Double click & import Action chains
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(3)
action = ActionChains(driver)
ele = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
action.double_click(ele).perform()    #This is for double click
time.sleep(3)
#action.context_click(ele).perform()   #This is for right click: Selenium cannot control browser menus (Back/Forward/Reload/Inspect) so never use context_click on normal buttons

#Drag & drop
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(3)
action = ActionChains(driver)
s = driver.find_element(By.ID, 'draggable')
d = driver.find_element(By.ID, 'droppable')
action.drag_and_drop(s,d).perform()
time.sleep(3)

#To upload file and to scroll
driver.get('https://practice-automation.com/file-upload/')
driver.execute_script("window.scroll(0,600)") # JS script to scroll
driver.find_element(By.XPATH, '//*[@id="file-upload"]').send_keys(r'C:\Users\Indraja Lakshmi\Desktop\Certifications\Selenium WebDriver with Python .pdf')
time.sleep(3)

#Cookies
driver.get("https://www.google.com")
cookies = driver.get_cookies()
for i in cookies:
    print(i)
time.sleep(3)

#Ajax
#Implicit wait driver.implicitly_wait(30)
#Explicit wait expected_conditions

driver.quit()
