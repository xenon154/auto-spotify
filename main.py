from env_vars import USERNAME, PASSWORD, BROWSER
from selenium import webdriver
from time import sleep
from webdriver_manager import chrome, firefox

driver = webdriver.Firefox(firefox.GeckoDriverManager().install()) if BROWSER=='firefox' else webdriver.Chrome(chrome.ChromeDriverManager().install())
driver.get("https://accounts.spotify.com/en/login")

#username/password input boxes
driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div[2]/div[1]/input").send_keys(USERNAME)
driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/input").send_keys(PASSWORD)

#"log in" button
driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div[2]/div[4]/button").click()

sleep(50000)