class BookData:
    def __init__(self, name, released, numberOfPages):
        self.name = name
        self.released = released
        self.numberOfPages = numberOfPages

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs.get('name'), kwargs.get('released'), kwargs.get('numberOfPages'))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
