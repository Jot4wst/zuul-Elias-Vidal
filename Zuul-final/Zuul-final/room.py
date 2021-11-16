
class Room:
    def __init__(self, description):
        self.description = description
        self.exits = {}
        #Se agregan items
        self.items = {}
        self.npcs = {}

    def setExits(self, north, east, south, west, up, down):
        if(north != None):
            self.exits['north'] = north
        if(east != None):
            self.exits['east'] = east
        if(south != None):
            self.exits['south'] = south
        if(west != None):
            self.exits['west'] = west
        # Se agregan las salidas up y down
        if (up != None):
            self.exits['up'] = up
        if (down != None):
            self.exits['down'] = down
        return

    def setItem(self, item):
        self.items[item.name] = item

    # Get item quita de la habitacion el item seleccionado
    def getItem(self, item):
        if(item in self.items):
            return self.items.pop(item)
        else:
            return None
    
    def getDescription(self):
        return self.description

    # Se agrega printLocationInfo
    def print_location_info(self):
        print("-> Estas " + self.getDescription())
        print("Salidas: ")
        exits = '| '
        for direction in self.exits.keys():
            exits += direction + ' | '
        print(exits)
        self.print_items_information()
        self.print_npcs()

    #Se agrega el metodo mostrar items
    def print_items_information(self):
        print("Items en la habitacion: ")
        items = '| '
        for item in self.items.keys():
            items += self.items[item].name + ' | '
        print(items)
        

    #Se agrega el metodo get_exit
    def get_exit(self, direction):
        if(direction in self.exits):
            return self.exits[direction]
        else:
            return None

    #Coloca el npc en la habitacion
    def setNpc(self, npc):
        self.npcs[npc.name] = npc

    # Chequear si el npc esta en la sala actual
    def checkNpc(self, npc):
        if(npc in self.npcs):
            return True
        else:
            return False

    def print_npcs(self):
        print("Npc en la habitacion: ")
        npcs = '| '
        for npc in self.npcs.keys():
            npcs += self.npcs[npc].name + ' | '
        print(npcs)