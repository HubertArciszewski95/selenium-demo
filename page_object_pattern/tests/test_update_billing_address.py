from random import randint
import pytest

# Import page objects
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.nav_bar import NavBar
from page_object_pattern.pages.my_account_page import MyAccountPage
from page_object_pattern.pages.my_account_page import MyAccountMenuPage
from page_object_pattern.pages.my_account_page import AddressPage
from page_object_pattern.pages.billing_address_page import BillingAddressPage


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        email = str(f"test{randint(1, 1001)}@test.com")

        home_page = HomePage(self.driver)
        home_page.open_page()

        nav_bar = NavBar(self.driver)
        nav_bar.click_my_account_link()

        my_account_page = MyAccountPage(self.driver)
        my_account_page.register(email, "testeroprogramowania")

        my_account_menu_page = MyAccountMenuPage(self.driver)
        my_account_menu_page.click_address_link()

        address_page = AddressPage(self.driver)
        address_page.click_billing_edit_link()

        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.set_personal_data("Hubert", "Test")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Kwiatowa 1", "00-001", "Gdańsk")
        billing_address_page.set_phone_number("111-111-111")
        billing_address_page.click_save_address_button()

        success_msg = "Address changed successfully."
        assert success_msg in address_page.get_billing_success_msg()

