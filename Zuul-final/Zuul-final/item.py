class Item:

    def __init__(self, name, description, weight, picked_up = True, snack=False, magico=False):
        self.name = name
        self.description = description
        self.weight = weight
        self.picked_up = picked_up
        self.snack = snack
        self.magico = magico

class Mision(Item):

    def __init__(self, name, description, weight, mision, picked_up = True, snack=False, magico=False):
        super().__init__(name, description, weight, picked_up, snack, magico)
        self.mision = mision

class Transportador(Item):

    def __init__(self, name, description, weight, picked_up = True, snack=False, magico=False):
        super().__init__(name, description, weight, picked_up, snack, magico)
        self.room_back = None
    
    def activado(self):
        return self.room_back is not None