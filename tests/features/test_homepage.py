from typing import Generator, Text
from screenpy import Actor, then, when, given
from screenpy.abilities import BrowseTheWeb
from screenpy.actions import Open, See
from screenpy.pacing import act, scene
from screenpy.questions import TheText, BrowserTitle
from screenpy.resolutions import ReadsExactly
from ..ui.homepage import MAIN_HEADING, URL

import pytest

@pytest.fixture(scope="function", name="Yuli")
def fixture_actor(selenium) -> Generator:
    """Create the Actor for our example tests!"""
    the_actor = Actor.named("Yuli").who_can(BrowseTheWeb.using(selenium))
    yield the_actor
    the_actor.exit_stage_left()

@pytest.mark.nondestructive
@act("Homepage")
@scene("See the title of pybaq page")
def test_homepage_title(Yuli: Actor) -> None:
    when(Yuli).was_able_to(Open.their_browser_on(URL))
    then(Yuli).should(See.the(BrowserTitle(), ReadsExactly("Python Barranquilla")))

@pytest.mark.nondestructive
@act("Homepage")
@scene("See the heading of pybaq page")
def test_homepage_h1(Yuli: Actor) -> None:
    when(Yuli).was_able_to(Open.their_browser_on(URL))
    then(Yuli).should(See.the(TheText.of_the(MAIN_HEADING), ReadsExactly("Python Barranquilla.")))