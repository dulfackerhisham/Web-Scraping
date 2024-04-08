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


"""
1 => find the element(Set of supported locator strategies) and by which element you want to find the data's
"""
# class name, tag name, name,xpath, partial link text, link text, id

# ---- xpath
# input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('Facebook')
# input.send_keys('Facebook')

# search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
# search.click()


# ---- partial link text
driver.find_element(By.PARTIAL_LINK_TEXT, 'മലയാളം').click()