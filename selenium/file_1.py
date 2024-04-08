from selenium import webdriver
from selenium.webdriver.chrome.service import Service #A Service class that is responsible for the starting and stopping of chromedriver
from webdriver_manager.chrome import ChromeDriverManager #installs driver which is responsible for connecting selenium and the browser
from selenium.webdriver.chrome.options import Options #can set up many things like 'when to stop chrome etc..'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.google.com/")