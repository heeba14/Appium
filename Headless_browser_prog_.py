from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# instantiate a chrome options object so you can set the size and headless preference
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
options.add_argument('--disable-gpu')
options.add_argument('--headless')
chrome_driver_path = "C:\\Users\\dell store\\PycharmProjects\\untitled1\\Drivers\\chromedriver.exe"
#chrome_driver = os.getcwd() +"\\chromedriver.exe"
# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver_path)
driver.get("https://www.google.com")
print(driver.title)
lucky_button = driver.find_element_by_css_selector("[name=btnI]")
lucky_button.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")