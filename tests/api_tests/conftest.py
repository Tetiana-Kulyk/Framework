import pytest
from data_objects.character_data import CharacterData
from data_objects.book_data import BookData
from data_objects.house_data import HouseData


@pytest.fixture()
def character_mock():
    return CharacterData(name='Jon Snow', culture='Northmen', gender="Male", born='In 283 AC')


@pytest.fixture()
def house_mock():
    return HouseData(name="House Targaryen of King's Landing", region='The Crownlands',
                     coatOfArms='Sable, a dragon thrice-headed gules')


@pytest.fixture()
def book_mock():
    return BookData(name='A Game of Thrones', released='1996-08-01T00:00:00', numberOfPages=694)
