from utilities.api.base_api import BaseAPI


class HousesAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.houses_url = '/houses/'

    def get_house(self, house_id, headers=None):
        response = self.get(url=f'{self.houses_url}{house_id}', headers=headers)
        return response
