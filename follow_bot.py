import requests
import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Rendering the Javascript to pass HTML to BeautifulSoup 
driver = webdriver.Firefox()

# Login to instagram
url = "https://www.instagram.com/accounts/login/"
driver.get(url)

username = "tensuixx"
password = "1234567m"

usr_element = wait(driver,10).until(EC.presence_of_element_located((By.NAME, "username")))
pw_element = driver.find_element_by_name("password")

usr_element.send_keys(username)
pw_element.send_keys(password,Keys.ENTER)

wait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"_8-yf5 "))) 

# Get username and follower count
url = "https://www.instagram.com/renides_eller/"
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')

stats = soup.find_all("span",{"class":"g47SY"})

username =  soup.find("h1",{"class":"_7UhW9 fKFbl yUEEX KV-D4 fDxYl"}).contents[0]
followers = stats[1]["title"].replace(",","")

# Open up hidden followers window
follow_element = driver.find_element_by_xpath("//a[@class='-nal3 ']")

follow_element.click()

# Load all followers
followers_element = wait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.isgrP")))

# Buffer through the 'suggestions for you'
for a in range(7):
    followers_element.send_keys(Keys.ARROW_DOWN)

followers_element.send_keys(Keys.ARROW_UP)
followers_element.send_keys(Keys.ARROW_UP)

for i in range(int(int(followers)*1.75)):
    followers_element.send_keys(Keys.ARROW_DOWN)

# Follow all followers
button_element = driver.find_elements_by_css_selector("button")

for j in range(len(button_element)):

    if button_element[j].get_attribute("class") == "sqdOP  L3NKy   y3zKF     ":
        button_element[j].click()
        time.sleep(6.9)
