# test_addition.py
from src.calculator import  add
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.chrome(ChromeDriverManager().install())
import pytest
import time


def test_add():
    result = add(3, 4)
    assert result == 7
def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)
def test_SMDB():
    driver.get('https://test-outsystems.de.bosch.com/SensorTrackingMetaData_Solution/')
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@role="menuitem" and text()="Treatments"]').click()
    time.sleep(5)
    driver.quit()