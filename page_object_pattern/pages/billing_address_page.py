from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BillingAddressPage:

    def __init__(self, driver):
        # Create driver object
        self.driver = driver

    # Create Page objects
        #
        # --- Billing address ---
        #
        self.first_name_input = (By.ID, "billing_first_name")
        self.last_name_input = (By.ID, "billing_last_name")
        self.country_select = (By.ID, "billing_country")
        self.street_address1_input = (By.ID, "billing_address_1")
        self.postcode_input = (By.ID, "billing_postcode")
        self.city_input = (By.ID, "billing_city")
        self.phone_number_input = (By.ID, "billing_phone")
        self.save_address_button = (By.XPATH, "//button[text()='Save address']")

    # Create Methods
    #
    # --- Billing address form methods ---
    #
    def set_personal_data(self, first_name, last_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city):
        self.driver.find_element(*self.street_address1_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    def set_phone_number(self, number):
        self.driver.find_element(*self.phone_number_input).send_keys(number)

    def click_save_address_button(self):
        self.driver.find_element(*self.save_address_button).click()


