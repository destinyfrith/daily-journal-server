# Classes need to be instantiated to create an object from its design.

class Entry():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, date, entry, concept, mood_id):
        self.id = id
        self.date = date
        self.entry = entry
        self.concept = concept
        self.mood_id = mood_id
        self.mood = None

        # code we would write to make a new object
        # new_entry = Entry(1, "Snickers", "Dog", "Recreation", 1, 4)