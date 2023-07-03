from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

option = webdriver.FirefoxOptions()
#option.add_argument("--headless")
option.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
driverService = Service('C:\\5SIMU\\python-test-calculator\\WebDriver\\geckodriver.exe')
driver = webdriver.Firefox(service=driverService, options=option)

def test_simo():

    driver.get("https://docs.pytest.org/en/7.3.x/")
    searchField = driver.find_element(By.NAME, "q")
    searchField.send_keys("test")
    searchField.send_keys(Keys.ENTER)
    assert "test" in driver.current_url
    driver.quit()
