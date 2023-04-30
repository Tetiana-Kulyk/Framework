class CharacterData:
    def __init__(self, name, culture, gender, born):
        self.name = name
        self.culture = culture
        self.gender = gender
        self.born = born

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs.get('name'), kwargs.get('culture'), kwargs.get('gender'), kwargs.get('born'))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
