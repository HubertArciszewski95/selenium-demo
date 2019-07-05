import pytest

# Import page objects
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.nav_bar import NavBar
from page_object_pattern.pages.my_account_page import MyAccountPage
from page_object_pattern.pages.my_account_page import MyAccountMenuPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_passed(self):
        home_page = HomePage(self.driver)
        home_page.open_page()

        nav_bar = NavBar(self.driver)
        nav_bar.click_my_account_link()

        my_account_page = MyAccountPage(self.driver)
        my_account_page.login("test@test.com", "testeroprogramowania")

        my_account_menu_page = MyAccountMenuPage(self.driver)
        assert my_account_menu_page.logout_link_is_displayed()

    def test_login_failed(self):
        home_page = HomePage(self.driver)
        home_page.open_page()

        nav_bar = NavBar(self.driver)
        nav_bar.click_my_account_link()

        my_account_page = MyAccountPage(self.driver)
        my_account_page.login("test@test.com", "ThisIsNotAPassword")

        error_msg = "ERROR: Incorrect username or password."
        assert error_msg in my_account_page.get_incorrect_username_or_password_message()
