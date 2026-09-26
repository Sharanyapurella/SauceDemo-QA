from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    # Start Chrome
    driver = webdriver.Chrome()

    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Enter username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click Login
    driver.find_element(By.ID, "login-button").click()

    # Verify Products page
    products = driver.find_element(By.CLASS_NAME, "title").text
    assert products == "Products"

    # Close Chrome
    driver.quit()