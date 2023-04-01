"""Locators de la pagina de inicio"""

from selenium.webdriver.common.by import By
from screenpy_selenium import Target

MAIN_HEADING = Target.the("Main heading").located((By.TAG_NAME, "h1"))
