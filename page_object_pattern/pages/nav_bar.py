from selenium.webdriver.common.by import By


class NavBar:

    def __init__(self, driver):
        # Create driver object
        self.driver = driver

    # Create Page objects
        # --- My account ---
        self.my_account_link = (By.XPATH, "//li[@id='menu-item-22']//a")

    # Methods
    # --- My Account methods ---
    # Perform click on "My Account"
    def click_my_account_link(self):
        self.driver.find_element(*self.my_account_link).click()

