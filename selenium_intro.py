# You need to install selenium and a webdriver (e.g., ChromeDriver)
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()  # Or webdriver.Edge(), etc.
driver.get("https://www.emirates.com/in/english/book/featured-fares/")

# Wait for page to load
time.sleep(3)

# Click the business class tab (find by text or class)
business_tab = driver.find_element("xpath", '/html/body/div[1]/main/div[2]/div/div[5]/div[1]/div[3]/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]')
business_tab.click()
time.sleep(2)  # Wait for content to update

soup = BeautifulSoup(driver.page_source, "html.parser")
fare_divs_bus_span = soup.find("span", class_="feature-fare-cabin-tabs__price-text")
if fare_divs_bus_span:
    print(fare_divs_bus_span.text.strip("*"))
else:
    print("Business class fare not found.")

driver.quit()