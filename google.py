import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_search_correct(window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_incorrect(window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('hfjh ejfhej ejhkw cejkdjn  djkjdh ewjkndw').press_enter()
    browser.element('[id="topstuff"]').should(have.text(' ничего не найдено. '))