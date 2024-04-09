from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.maximize_window()
driver.get("https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy,4io")

iphone_name = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[1]/div[1]').text
iphone_disc_price = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]').text
iphone_og_price = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[2]').text
discount = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[3]/span').text
rating = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[1]/div[2]/span[1]/div').text
ratings = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[1]').text
reviews = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[3]').text

print('----------------------------------------------')
print(f'mobile -> {iphone_name}')
print(f'original price -> {iphone_og_price} === discount price -> {iphone_disc_price}')
print(f'original price -> {discount}')
print(f'rating -> {rating} , {ratings}')
print(f'total reviews -> {reviews}')