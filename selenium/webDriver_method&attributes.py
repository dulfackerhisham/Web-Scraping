from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://www.google.com/")

#getting page source
page_source = driver.page_source
print(f'page source => {page_source}')

#html title
title = driver.title
print(f'title => {title}')

#current url
print(f'current url => {driver.current_url}')

window_position = driver.get_window_position(windowHandle='current')
print(f'windown position => {window_position}')

window_rect = driver.get_window_rect()
print(f'window rect {window_rect}')

window_size = driver.get_window_size
print(f'windown size => {window_size}')

driver.minimize_window()

# driver.close()
driver.quit()