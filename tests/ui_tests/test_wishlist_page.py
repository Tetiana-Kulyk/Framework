import pytest


@pytest.mark.regression
@pytest.mark.wishlist
def test_check_monitor_price_checkbox(check_monitor_price):
    assert check_monitor_price.is_price_checkbox_checked(), 'The "monitor price" checkbox is not checked'


@pytest.mark.regression
@pytest.mark.wishlist
def test_notify_about_availability(notify_about_availability):
    assert notify_about_availability.is_notify_about_availability_checkbox_checked(), 'The "notify about ' \
                                                                                      'availability" checkbox is ' \
                                                                                      'not unchecked'


@pytest.mark.regression
@pytest.mark.wishlist
def test_add_to_basket_and_continue_shopping(add_to_basket_from_wishlist):
    assert add_to_basket_from_wishlist.is_wishlist_page_opened(), 'Wishlist page is not opened'
