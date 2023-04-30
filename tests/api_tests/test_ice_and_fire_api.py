from http import HTTPStatus
from data_objects.character_data import CharacterData
from data_objects.book_data import BookData
from data_objects.house_data import HouseData

from api_collections.characters_api import CharactersAPI
from api_collections.books_api import BooksAPI
from api_collections.houses_api import HousesAPI


def test_character_api(env, character_mock):
    expected_character = character_mock
    response = CharactersAPI(env).get_character(583)
    response_data = response.json()
    actual_character = CharacterData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_character == expected_character, 'Character data is not as expected'


def test_house_api(env, house_mock):
    expected_house = house_mock
    response = HousesAPI(env).get_house(378)
    response_data = response.json()
    actual_house = HouseData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_house == expected_house, 'House data is not as expected'


def test_book_api(env, book_mock):
    expected_book = book_mock
    response = BooksAPI(env).get_book(1)
    response_data = response.json()
    actual_book = BookData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_book == expected_book, 'Book data is not as expected'
