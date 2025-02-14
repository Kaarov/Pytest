class Person(object):
    def __init__(self, name, favorite_animal=None):
        self.name = name
        self.favorite_animal = favorite_animal


def anyone_like_dogs(people):
    """Check if 1 person likes dogs."""
    return any(
        [person.favorite_animal == "dog" for person in people]
    )
