import pytest

@pytest.fixture
def api_context(playwright):
    ctx = playwright.request.new_context(base_url="https://apidev.emversity.com")
    yield ctx
    ctx.dispose()
