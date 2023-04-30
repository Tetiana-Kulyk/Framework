from utilities.api.base_api import BaseAPI


class BooksAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.books_url = '/books/'

    def get_book(self, book_id, headers=None):
        response = self.get(url=f'{self.books_url}{book_id}', headers=headers)
        return response
