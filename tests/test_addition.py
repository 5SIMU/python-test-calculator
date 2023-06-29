# # test_addition.py
# from src.calculator import  add
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from chromedriver_py import binary_path
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import pytest
# import time
#
# @pytest.fixture()
# def test_setup():
#     service_object = Service(binary_path)
#     global driver
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--ignore-certificate-errors")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--disable-popup-blocking")
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--window-size=1920x1080")
#     driver = webdriver.Chrome(service=service_object,options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield
#     driver.quit()
#
# def test_add():
#     result = add(3, 4)
#     assert result == 7
# def test_add_string():
#     with pytest.raises(TypeError):
#         add("string", 4)
# def test_SMDB(test_setup):
#     driver.get("https://docs.pytest.org/en/7.3.x/")
#     searchField = driver.find_element(By.NAME, "q")
#     searchField.send_keys("test")
#     searchField.send_keys(Keys.ENTER)
#     assert "test" in driver.current_url
