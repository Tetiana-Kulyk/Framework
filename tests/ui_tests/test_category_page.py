import pytest


@pytest.mark.category
@pytest.mark.regression
def test_search_item(open_hair_category_page):
    assert open_hair_category_page.search_item().is_searched_item_displayed(), "Searched item is not shown in results"
