from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

def test_title(base_url):
    selenium = Chrome()
    selenium.get(base_url)
    assert selenium.title == "Python Barranquilla"

def test_main_heading(base_url):
    selenium = Chrome()
    selenium.get(base_url)
    assert selenium.find_element(by=By.TAG_NAME, value='h1').text == "Python Barranquilla."
