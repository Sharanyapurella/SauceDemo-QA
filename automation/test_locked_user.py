from selenium import webdriver
from selenium.webdriver.common.by import By


def test_locked_user():
    # Start Chrome
    driver = webdriver.Chrome()

    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Enter locked user credentials
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click Login
    driver.find_element(By.ID, "login-button").click()

    # Get error message
    error_message = driver.find_element(
        By.CSS_SELECTOR,
        "h3[data-test='error']"
    ).text

    # Verify locked user error
    assert "Epic sadface: Sorry, this user has been locked out." in error_message

    # Close Chrome
    driver.quit()