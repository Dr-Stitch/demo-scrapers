from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
# from openpyxl import Workbook, load_workbook
# from openpyxl.utils import get_column_letter as cell

def search(driver, value):
          try:
                    full_input_box = driver.find_element(By.XPATH, '/html/body/div[2]/form/div[3]/div[2]/section/div/div/div/div/div[3]')
                    input_box = full_input_box.find_element(By.ID, 'acdee324')
                    search_button = full_input_box.find_element(By.XPATH, "//*[@class = 'Search pzhc pzbutton']")
                    input_box.clear()
                    input_box.send_keys(value)         
                    search_button.click()
                    time.sleep(.7)
                    Search_result = driver.find_elements(By.XPATH, "/html/body/div[2]/form/div[3]/div[2]/section/div/div/div/div/div[5]")
                    for result in Search_result:

                              try:
                                        index.append(result.find_element(By.XPATH, '//*[@class= "content-item content-field item-1 flex flex-row text-extra-bold dataValueRead"]').text)
                                        address.append(result.find_element(By.XPATH, '//*[@data-expr-id="92d84abc27ead390e253e29caad0e63ce88b40e0_7"]').text)
                                        space.append(result.find_element(By.XPATH, '//*[@class="content-item content-field item-4 flex flex-row dataValueRead"]').text)
                                        dates = result.find_elements(By.XPATH, '//*[@class="field-item dataValueRead"]')
                                        date.append(dates[1].text)
                                        df = pd.DataFrame({'Index':index, 'Addess': address, 'Space': space, 'Registered on': date})
                                        df.to_excel('nsw.gov4.xlsx', index=False)
                              except:
                                      pass
          except:
                  pass
          
          
          
website = 'https://www.stratahub.nsw.gov.au/prweb/PRAuth/app/ssr_4380/mashup/!SchemeSearch/?pzuiactionzzz=CXtpbn15a2gyQTl4dnV4YlN5TzhpbE5uYU1ielJHYmsxUVc0Nk9nR2Y0dmFtT1hldkQya0JnNi9Wc2dCK3hQOWJ0VytoZUZnTnd0YTdTc2M5TVZ4Sjh0Z1JMWXJWTEFBc3Q0cUlScEs3eEFyR3VwQkZvSkV0eUZSSVQ1Tm9IREx1bi9ZUERyd3UrQjBCc3BTSmk4em9zKzhkSGptNm9hSXBBb012bXRQTzVXK0lERHpNVVMzRmtCUHhMY3gyN1NFWSt2Z2l4cHFSMHZQRmFZQTVCSzFFSjNpcnBTZ3VXUHlzNGxPWTB2U2hPZDVLSm1vYlVYZUNxL3JQYjhaOVJBeThHUzFseU9VRDdENXV3aU9PaVN6TktTQ2JrTWkwZVd1UG55a29aSHh6V1V5YWhTSUxLbmY5SmF1ZVZZSEpIT1dnRTY5QlBnaHc3SzhjbGVRcDBaL3FvK3ovMlhhZVJSWkJHSW4xSXZJQTdmYktUVVpTRWs1V3JtYmE1NXduL3BrRmdSTEx4b2pwOXlSanFSMjdoT1ArRVlxWnBBPT0%3D*'
driver = webdriver.Edge()
# driver.maximize_window()
driver.get(website)

options = Options()  # Initialize an instance of the Options class
options.headless = True  # True -> Headless mode activated
options.add_argument('window-size=1920x1080')  # Set a big window size, so all the data will be displayed

full_check_box = driver.find_element(By.XPATH , "/html/body/div[2]/form/div[3]/div[2]/section/div/div/div/div/div[2]")
SPN_button = full_check_box.find_element(By.XPATH, "//*[@id='RULE_KEY']/div/div/div/div[2]/div/div/div/div/div[2]/span/label")
SPN_button.click()
time.sleep(1)

index = []
address=[]
space=[]
date=[]
for i in range(3885,120000):
        search(driver, i)

# df = pd.DataFrame({'Index':index, 'Addess': address, 'Space': space, 'Registered on': date})
# df.to_excel('nsw.gov.xlsx', index=False)
