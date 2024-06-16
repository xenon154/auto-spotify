from env_vars import USERNAME, PASSWORD
from selenium import webdriver
from time import sleep

cService = webdriver.ChromeService(executable_path='/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(service=cService)
driver.get("https://accounts.spotify.com/en/login")

#username/password input boxes
driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div[2]/div[1]/input").send_keys(USERNAME)
driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/input").send_keys(PASSWORD)

#"log in" button
driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div[2]/div[4]/button").click()

sleep(50000)