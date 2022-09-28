from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
import numpy as np

url = 'https://bringatrailer.com/models/'
options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options= options)
driver.get(url)

print('')
print('')

models = driver.find_elements(By.CLASS_NAME, 'previous-listing-image-overlay-inner-cell')
model = random.choice(models)
model.click()

cars = driver.find_elements(By.CLASS_NAME, 'title')
sold_for = driver.find_elements(By.CLASS_NAME, 'subtitle')
car_list = []
sold_list = []

for car in cars:
    car_list.append(car.text)
for sold in sold_for:
    sold_list.append(sold.text)
   
for x in range(len(cars)):    
    print(car_list[x-1])
    print(sold_list[x-1])
    print('')

print('')
print('')
