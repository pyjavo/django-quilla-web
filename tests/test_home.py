"""
Test de homepage usando selenium sin ayudas, (sin patrones, tipo POM o algo por el estilo)
"""

from selenium.webdriver.common.by import By

def test_title(base_url, driver):
    """Test de la página de inicio"""
    driver.get(base_url)
    assert driver.title == "Python Barranquilla"
    assert driver.find_element(by=By.TAG_NAME, value='h1').text == "Python Barranquilla."
    driver.quit()
