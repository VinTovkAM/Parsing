from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


custom_options = Options()
custom_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=custom_options) 
link = 'https://www.flashscorekz.com/'
driver.get(link)

match_sp = []

driver_m = driver.find_elements(By.CLASS_NAME, 'event__match.event__match--withRowLink.event__match--scheduled.event__match--twoLine')
for element in driver_m:
    match_sp.append(element.text.splitlines())


columns_name = ['status', 'team_1', 'team_2', 'g_1', 'g_2']
result = pd.DataFrame(match_sp, columns=columns_name)
result.to_excel('game.xlsx', index=False)
driver.quit()
