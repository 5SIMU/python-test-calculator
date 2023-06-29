import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

def test_simo():
    driver.get("https://docs.pytest.org/en/7.3.x/")
    driver.maximize_window()
    searchField = driver.find_element(By.NAME, "q")
    searchField.send_keys("test")
    searchField.send_keys(Keys.ENTER)
    assert "test" in driver.current_url