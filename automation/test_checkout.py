from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout():

    # Start Chrome
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:

        # --------------------------------
        # 1. Open SauceDemo
        # --------------------------------
        driver.get("https://www.saucedemo.com/")

        # --------------------------------
        # 2. Login
        # --------------------------------
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        ).send_keys("standard_user")

        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID, "login-button"
        ).click()

        # --------------------------------
        # 3. Add product to cart
        # --------------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        # --------------------------------
        # 4. Open cart
        # --------------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

        # --------------------------------
        # 5. Click Checkout
        # --------------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()

        # --------------------------------
        # 6. Enter customer information
        # --------------------------------
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        ).send_keys("Sharanya")

        driver.find_element(
            By.ID, "last-name"
        ).send_keys("Purella")

        driver.find_element(
            By.ID, "postal-code"
        ).send_keys("500001")

        # --------------------------------
        # 7. Click Continue
        # --------------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        ).click()

        # --------------------------------
        # 8. Wait for Checkout Overview
        # --------------------------------
        wait.until(
            EC.url_contains("checkout-step-two.html")
        )

        # --------------------------------
        # 9. Verify Checkout Overview
        # --------------------------------
        checkout_title = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        print("Current page:", checkout_title.text)

        assert checkout_title.text == "Checkout: Overview"

        # --------------------------------
        # 10. Click Finish
        # --------------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "finish")
            )
        ).click()

        # --------------------------------
        # 11. Verify Order Confirmation
        # --------------------------------
        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        print("Confirmation:", confirmation.text)

        assert confirmation.text == "Thank you for your order!"

    finally:

        # Close browser
        driver.quit()