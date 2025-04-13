import allure
from allure_commons._allure import title

from wikipedia.pages import wikipedia_app

@allure.epic("Wikipedia")
@allure.feature("Search")
@allure.story("Search valid query")
class TestSearch:
    @title("Search and verify found content")
    def test_search(self, search_query="Appium"):
        wikipedia_app.type_search(search_query)
        wikipedia_app.verify_content_found(search_query)

    @title("Search and open article")
    def test_search_and_open_article(self, search_query="Appium"):
        wikipedia_app.type_search(search_query)
        wikipedia_app.open_article(search_query)
