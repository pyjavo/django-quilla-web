"""
Configuración de test automatizados
"""

import os
from typing import Generator
import pytest
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(name="driver")
def fixture_driver() -> Generator:
    """Creamos el webdriver que vamos a usar en nuestros tests!"""
    posible_options = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions()
    }
    browser = os.getenv("TEST_BROWSER", "chrome")
    command_executor = os.getenv("TEST_COMMAND_EXECUTOR", "http://127.0.0.1:4444/wd/hub")
    options = posible_options[browser]
    driver = Remote(command_executor=command_executor, options=options)
    yield driver
