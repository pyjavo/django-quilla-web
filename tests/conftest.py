"""
Configuración de test automatizados
"""

from typing import Generator
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(name="driver")
def fixture_driver() -> Generator:
    """Creamos el actor que vamos a usar en nuestros tests!"""
    driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=Options())
    yield driver
