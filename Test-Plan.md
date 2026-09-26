# SauceDemo QA Test Plan

Website:https://www.saucedemo.com/

Project:
SauceDemo Website Testing

Tester: Sharanya Purella

Testing Type: Manual Testing

# SauceDemo QA Test Plan

## 1. Objective

The objective of this test plan is to test the main functionality of the SauceDemo e-commerce website and identify functional, UI, negative, edge-case, and performance-related issues.

The testing covers login, product browsing, product sorting, shopping cart, and checkout functionality.

## 2. Scope

### In Scope

- User login and authentication
- Product browsing
- Product details
- Product sorting
- Add product to cart
- Remove product from cart
- Cart validation
- Checkout form
- Checkout overview
- Order completion

### Out of Scope

- Payment gateway integration
- Real payment processing
- Backend/database testing
- Sauce Labs account management

## 3. Testing Types

### Functional Testing

Verify that the main features of the SauceDemo website work as expected, including login, product browsing, sorting, cart, and checkout.

### UI Testing

Verify that buttons, text fields, product images, prices, menus, and other user-interface elements are displayed and behave correctly.

### Negative Testing

Test invalid or restricted situations, such as locked-out users and submitting checkout forms without required information.

### Edge Case Testing

Test situations such as removing products from the cart, empty or incomplete checkout information, and other boundary conditions.

### Cross-Browser Testing

Test the website using different web browsers to identify browser-specific issues.
## 4. Test Environment

| Item | Details |
|---|---|
| Operating System | Windows |
| Browser | Google Chrome |
| Website | https://www.saucedemo.com/ |
| Testing Method | Manual Testing |
| Internet Connection | Active |
## 5. Test Data

| Username | Password | Purpose |
|---|---|---|
| standard_user | secret_sauce | Standard user testing |
| locked_out_user | secret_sauce | Locked account testing |
| problem_user | secret_sauce | Testing application problems |
| performance_glitch_user | secret_sauce | Performance testing |

## 6. Test Cases

| TC ID | Test Scenario | Preconditions | Test Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|
| TC-001 | Valid Login | User is on the SauceDemo login page | 1. Enter valid username 2. Enter password 3. Click Login | User should be logged in and redirected to the Products page | User was redirected to the Products page | Pass |
| TC-002 | Locked User Login | User is on the SauceDemo login page | 1. Enter locked_out_user 2. Enter password 3. Click Login | An error message should be displayed for the locked user | The locked user error message was displayed | Pass |
| TC-003 | Add Product to Cart | User is logged in | 1. Select a product 2. Click Add to cart 3. Open the cart | Selected product should be added to the cart | Product was added to the cart | Pass |
| TC-004 | Checkout Required Fields | Product is available in the cart | 1. Open cart 2. Click Checkout 3. Leave required fields empty 4. Continue | Required-field validation messages should be displayed | Required-field validation was displayed | Pass |
| TC-005 | Product Sorting | User is logged in | 1. Open Products page 2. Select a sorting option | Products should be displayed according to the selected sorting option | Sorting did not work correctly during testing | Fail |
## 7. Risk Assessment

| Risk | Impact | Priority | Mitigation |
|---|---|---|---|
| Login failure | Users may not be able to access the application | High | Test valid and locked user login scenarios |
| Incorrect product information | Users may receive incorrect product details | Medium | Verify product name, image, price, and description |
| Cart functionality failure | Users may not be able to add or remove products | High | Test adding and removing products from the cart |
| Checkout validation failure | Users may not be able to complete checkout | High | Test required checkout fields with valid and invalid data |
| Sorting failure | Users may have difficulty finding products | Medium | Test different product sorting options |
| Slow page loading | Users may experience delays while using the application | Medium | Observe page loading behavior during performance testing |
## 8. Test Plan Summary

The SauceDemo application was tested for login, product browsing, product sorting, shopping cart, and checkout functionality.

Different user accounts were used to test normal, locked, problem, and performance-related scenarios.

The testing included functional, UI, negative, and edge-case testing. Cross-browser testing was also considered as part of the test plan.

The issues identified during testing are documented separately in the Bug Report.