import pytest



#@pytest.mark.main
#@pytest.mark.regression
#def test_change_site_language(change_site_language):
    #assert change_site_language.is_site_language_ru(), 'Site language is not changed'


@pytest.mark.main
@pytest.mark.smoke
def test_open_hair_category_page(open_hair_category_page):
    assert open_hair_category_page.is_category_page_opened(), 'Hair category page is not opened'


@pytest.mark.main
@pytest.mark.smoke
def test_open_promotions_page(open_promotions_page):
    assert open_promotions_page.is_promotions_page_opened(), 'Promotions page is not opened'


@pytest.mark.main
@pytest.mark.smoke
def test_open_account_page(open_account_page):
    assert open_account_page.is_contact_info_page_opened(), 'Account page is not opened'
