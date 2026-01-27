import pytest

@pytest.fixture
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://fortytwoaidev.emversity.com")

    yield page

    context.close()
    browser.close()
