from random import randint
import pytest

# Import page objects
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.nav_bar import NavBar
from page_object_pattern.pages.my_account_page import MyAccountPage
from page_object_pattern.pages.my_account_page import MyAccountMenuPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_failed(self):
        home_page = HomePage(self.driver)
        home_page.open_page()

        nav_bar = NavBar(self.driver)
        nav_bar.click_my_account_link()

        my_account_page = MyAccountPage(self.driver)
        my_account_page.register("test@test.com", "testeroprogramowania")

        error_msg = "Error: An account is already registered with your email address. Please log in."
        assert error_msg in my_account_page.get_account_registered_error_message()

    def test_create_account_passed(self):
        email = str(f"test{randint(1, 1001)}@test.com")

        home_page = HomePage(self.driver)
        home_page.open_page()

        nav_bar = NavBar(self.driver)
        nav_bar.click_my_account_link()

        my_account_page = MyAccountPage(self.driver)
        my_account_page.register(email, "testeroprogramowania")

        my_account_menu_page = MyAccountMenuPage(self.driver)
        assert my_account_menu_page.logout_link_is_displayed()



