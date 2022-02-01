from selenium.webdriver.common.by import By
from screenpy import Target

URL = "https://pybaq.co"
MAIN_HEADING = Target.the("Main heading").located((By.TAG_NAME, "h1"))