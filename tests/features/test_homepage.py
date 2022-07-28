from typing import Generator
from screenpy import Actor, then, when
from screenpy_selenium.abilities import BrowseTheWeb
from screenpy.actions import See
from screenpy_selenium.actions import Open
from screenpy.pacing import act, scene
from screenpy_selenium.questions import TheText, BrowserTitle
from screenpy.resolutions import ReadsExactly
from ..ui.homepage import MAIN_HEADING, URL

import pytest

@pytest.fixture(scope="function", name="yuli")
def fixture_actor() -> Generator:
    """Create the Actor for our example tests!"""
    the_actor = Actor.named("Yuli").who_can(BrowseTheWeb.using_firefox())
    yield the_actor
    the_actor.exit_stage_left()

@act("Homepage")
@scene("See the title of pybaq page")
def test_homepage_title(yuli: Actor) -> None:
    when(yuli).was_able_to(Open.their_browser_on(URL))
    then(yuli).should(See.the(BrowserTitle(), ReadsExactly("Python Barranquilla")))

@act("Homepage")
@scene("See the heading of pybaq page")
def test_homepage_h1(yuli: Actor) -> None:
    when(yuli).was_able_to(Open.their_browser_on(URL))
    then(yuli).should(See.the(TheText.of_the(MAIN_HEADING), ReadsExactly("Python Barranquilla.")))