from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(15)
driver.get('https://www.google.com/')
