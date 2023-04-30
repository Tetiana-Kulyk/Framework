class HouseData:
    def __init__(self, name, region, coatOfArms):
        self.name = name
        self.region = region
        self.coatOfArms = coatOfArms

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs.get('name'), kwargs.get('region'), kwargs.get('coatOfArms'))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__