"""Test de homepage usando screenpy con el patron screenplay"""
from typing import Generator
import pytest
from screenpy import Actor, then, when
from screenpy.actions import See
from screenpy.pacing import act, scene
from screenpy.resolutions import ReadsExactly
from screenpy_selenium.abilities import BrowseTheWeb
from screenpy_selenium.actions import Open
from screenpy_selenium.questions import TheText, BrowserTitle
from ..ui.homepage import MAIN_HEADING

@pytest.fixture(scope="function", name="yuli")
def fixture_actor(driver) -> Generator:
    """Creamos el actor que vamos a usar en nuestros tests!"""
    the_actor = Actor.named("Yuli").who_can(BrowseTheWeb.using(driver))
    yield the_actor
    the_actor.exit_stage_left()

@act("Homepage")
@scene("Puede ver Python barranquilla")
def test_homepage_title(yuli: Actor, base_url) -> None:
    """Verificamos que en homepage se pueda ver python barranquilla"""
    when(yuli).was_able_to(Open.their_browser_on(base_url))
    then(yuli).should(See.the(BrowserTitle(), ReadsExactly("Python Barranquilla")))
    then(yuli).should(See.the(TheText.of_the(MAIN_HEADING), ReadsExactly("Python Barranquilla.")))
