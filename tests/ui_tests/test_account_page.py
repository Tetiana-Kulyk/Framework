import pytest


@pytest.mark.account
@pytest.mark.smoke
def test_logout(logout):
    assert logout.is_login_button_displayed(), 'Logout is not performed'


@pytest.mark.account
@pytest.mark.smoke
def test_open_contact_info_page(open_account_page):
    open_account_page.is_contact_info_page_opened(), 'Contact info page is not opened'


@pytest.mark.account
@pytest.mark.smoke
def test_open_address_book_tab(open_address_book_tab):
    assert open_address_book_tab.is_address_book_tab_active(), 'Address book tab is not opened'


@pytest.mark.account
@pytest.mark.smoke
def test_open_wishlist_tab(open_wishlist_tab):
    assert open_wishlist_tab.is_wishlist_tab_active(), 'Wishlist tab is not opened'


@pytest.mark.account
@pytest.mark.smoke
def test_open_orders_history_tab(open_orders_history_tab):
    assert open_orders_history_tab.is_orders_history_tab_active(), 'Orders history tab is not opened'


@pytest.mark.account
@pytest.mark.smoke
def test_open_wishlist(open_wishlist_tab):
    assert open_wishlist_tab.is_wishlist_tab_active(), 'Wishlist tab is not opened'
