#Be careful with webscrapping it might be illegal to do on certain websites
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
#Find path of the file

driver = webdriver.Chrome(PATH)
driver.get("https://www.techwithtim.net/")
print(driver.title) # print title of website

search = driver.find_element_by_name("s")
search.send_keys("Test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))

     )
    print(main.text)
except:
    driver.quit()

driver.quit()


#print(driver.page_source)- Prints the page source
#time.sleep(5) - Delay how long until the window closes
#driver.quit - Quits the window



