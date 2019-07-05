from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()



