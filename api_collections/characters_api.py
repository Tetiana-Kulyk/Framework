from utilities.api.base_api import BaseAPI


class CharactersAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.characters_url = '/characters/'

    def get_character(self, character_id, headers=None):
        response = self.get(url=f'{self.characters_url}{character_id}', headers=headers)
        return response
