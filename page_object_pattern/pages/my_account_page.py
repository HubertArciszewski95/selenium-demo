from selenium.webdriver.common.by import By


class MyAccountPage:
    # Available when user log out

    def __init__(self, driver):
        # Create driver object
        self.driver = driver

    # Create page objects
        #
        # --- Register ---
        #
        self.register_email_input = (By.ID, "reg_email")
        self.register_password_input = (By.ID, "reg_password")
        self.register_button = (By.NAME, "register")

        # Register error messages
        self.account_registered_error_message = (By.XPATH, "//ul[@class='woocommerce-error']//li")

        #
        # --- Login ---
        #
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[text()='Log in']")

        # Login error messages
        self.incorrect_username_or_password_message = (By.XPATH, "//ul[@class='woocommerce-error']//li")

    # Create Methods
    #
    # --- Register Methods ---
    #
    def register(self, email, password):
        # Type email
        self.driver.find_element(*self.register_email_input).send_keys(email)
        # Type password
        self.driver.find_element(*self.register_password_input).send_keys(password)
        # Click at "Register" button
        register_button = self.driver.find_element(*self.register_button)
        self.driver.execute_script("arguments[0].click()", register_button)

    # Register error messages
    def get_account_registered_error_message(self):
        return self.driver.find_element(*self.account_registered_error_message).text

    #
    # --- Login Methods ---
    #
    def login(self, email, password):
        # Type email
        self.driver.find_element(*self.username_input).send_keys(email)
        # Type password
        self.driver.find_element(*self.password_input).send_keys(password)
        # Click at "Log in" button
        login_button = self.driver.find_element(*self.login_button)
        self.driver.execute_script("arguments[0].click()", login_button)

    # Login error messages
    def get_incorrect_username_or_password_message(self):
        return self.driver.find_element(*self.incorrect_username_or_password_message).text


# Below class available when user login


class MyAccountMenuPage:

    def __init__(self, driver):
        # Create driver object
        self.driver = driver

    # Create page objects
        # --- My Account menu ---
        self.address_link = (By.LINK_TEXT, "Addresses")
        self.log_out_link = (By.LINK_TEXT, "Logout")

    # Create Methods
        # --- Address methods ---
    def click_address_link(self):
        self.driver.find_element(*self.address_link).click()

        # --- Logout methods ---
    def logout_link_is_displayed(self):
        return self.driver.find_element(*self.address_link).is_displayed()

# Below class available when user login


class AddressPage:

    def __init__(self, driver):
        # Create driver object
        self.driver = driver

    # Create page objects
        #
        # --- Address Page ---
        #
        self.billing_edit_link = (By.XPATH, "//div[@class='u-column1 col-1 woocommerce-Address']//a")

        # Success Messages
        self.billing_address_success_message = (By.XPATH, "//div[@class='woocommerce-message']")

    # Create Methods
    #
    # --- Billing address ---
    #
    def click_billing_edit_link(self):
        self.driver.find_element(*self.billing_edit_link).click()

    # Get billing success message
    def get_billing_success_msg(self):
        return self.driver.find_element(*self.billing_address_success_message).text



