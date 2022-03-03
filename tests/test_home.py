import pytest
from selenium.webdriver.common.by import By

@pytest.mark.nondestructive
def test_title(selenium, base_url):
    selenium.get(base_url)
    assert selenium.title == "Python Barranquilla"

@pytest.mark.nondestructive
def test_main_heading(selenium, base_url):
    selenium.get(base_url)
    assert selenium.find_element(by=By.TAG_NAME, value='h1').text == "Python Barranquilla."
