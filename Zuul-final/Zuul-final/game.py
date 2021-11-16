from room import Room
from parser_commands import Parser
from item import Item, Mision, Transportador
from stack import Stack, inverso
from player import Player
from npc import Npc

class Game:
    def __init__(self):
        self.createRooms()
        self.parser = Parser()
        self.stack = Stack()
        # Se agega al jugador la capacidad maxima que puede llevar(17)
        # y el peso llevado(0)
        self.player = Player('jugador', 17, 0)

    # Se crean las salas 
    def createRooms(self):
        outside = Room("afuera de la entrada principal de la empresa <-")
        hall = Room("en el pasillo <-")
        officeroom = Room("en la sala de oficinas <-")
        conferencehall = Room("en la sala de conferencias <-")
        bathroom = Room("en el cuarto de baños <-") 
        cleaningroom = Room("en el cuarto de limpieza <-")
        library = Room("en la biblioteca <-")
        restroom = Room("en el cuarto de descanso <-")
        lunchroom = Room("en la cafeteria <-")
        depositroom = Room("en el deposito <-")

        # Items:
        pantalla = Item('pantalla', 'Una pantalla de repuesto', 4)
        laptop = Item('laptop', 'Tu laptop', 2)
        silla = Item('silla', 'Una silla', 2)
        disco = Item('disco', 'Un disco memoria con tus trabajos', 0.2)
        microfono = Item('microfono', 'Un microfono', 0.3)
        tacho = Item('tacho', 'Un tacho de basura', 4)
        escoba = Item('escoba', 'Una escoba', 1.5)
        pala = Item('pala', 'Una pala de la basura', 2)
        snack = Item('snack', 'Una merienda', 0.2, snack=True)
        bebida = Item('bebida', 'Una bebida', 0.3)
        libro = Item('libro', 'Un libro de informatica', 0.3)
        lupa = Item('lupa', 'una lupa', 0.1)
        proyector = Item('proyector', 'Un proyector', 3)
        cuadro = Item('cuadro', 'un cuadro que podes cambiar de lugar', 0.3)
        folleto = Item('folleto', 'un folleto con los servicios de la empresa', 0.1)
        escritorio = Item('escritorio', 'Un escritorio', 8, picked_up=False)
        estanteria = Item('estanteria', 'una estanteria', 8, picked_up=False)
        heladera = Item('heladera', 'Una heladera', 15, picked_up=False)
        computadora = Item('computadora', 'Una computadora', 5)
        parlantes = Item('parlantes', 'Unos parlantes de repuesto', 4)
        maceta = Item('maceta', 'Una maceta con una planta', 5)
        galleta = Item('galleta', 'Galleta magica que aumenta tu fuerza', 0.1, snack=False, magico=True)
        juego = Item('juego', 'Un juego de mesa', 3)
        # Se colocan los items de las misiones 
        carta = Mision('carta', 'una carta', 0.1, 'mision: debes juntar una llave antigua')
        LlaveAntigua = Mision('LlaveAntigua', 'una llave antigua', 0.1, None)
        # Se agrega un item trnsportador 
        transportador = Transportador('transportador', 'un transportador', 1)

        # Se agregan NPC
        yoda = Npc('yoda')
        skywalker = Npc('skywalker')

        # Colocar items en las salas
        outside.setItem(transportador)
        officeroom.setItem(laptop)
        officeroom.setItem(escritorio)
        officeroom.setItem(silla)
        officeroom.setItem(disco)
        officeroom.setItem(LlaveAntigua)
        hall.setItem(cuadro)
        hall.setItem(folleto)
        hall.setItem(carta)
        conferencehall.setItem(microfono)
        conferencehall.setItem(proyector)
        conferencehall.setNpc(skywalker)
        cleaningroom.setItem(escoba)
        cleaningroom.setItem(pala)
        cleaningroom.setItem(tacho)
        lunchroom.setItem(snack)
        lunchroom.setItem(bebida)
        lunchroom.setItem(heladera)
        lunchroom.setNpc(yoda)
        lunchroom.setItem(galleta)
        library.setItem(libro)
        library.setItem(estanteria)
        library.setItem(lupa)
        depositroom.setItem(pantalla)
        depositroom.setItem(computadora)
        depositroom.setItem(parlantes)
        restroom.setItem(maceta)
        restroom.setItem(juego)
        
        
        # Establecer salidas
        outside.setExits(None, None, hall, None, None, None)
        hall.setExits(outside, library, officeroom, cleaningroom, None, None)
        officeroom.setExits(hall, lunchroom, conferencehall, bathroom, restroom, depositroom)
        conferencehall.setExits(officeroom, None, None, None, None, None)
        bathroom.setExits(cleaningroom, officeroom, None, None, None, None)
        cleaningroom.setExits(None, hall, bathroom, None, None, None)
        library.setExits(None, None, lunchroom, hall, None, None)
        restroom.setExits(None, None, None, None, None, officeroom)
        lunchroom.setExits(library, None, None, officeroom, None, None)
        depositroom.setExits(None, None, None, None, officeroom, None)

        self.currentRoom = outside
        
        return

    def play(self):
        self.printWelcome()
        
        finished = False
        while(not finished):
            command = self.parser.getCommand()
            finished = self.processCommand(command)
        print("Gracias por jugar. Hasta luego!")

    def printWelcome(self):
        print()
        print("Bienvenido a la empresa!")
        print("Explora y conoce la instalacion")
        print("Escribe 'help' si necesitas ayuda")
        print("")
        # Modificacion printLocationInfo
        self.currentRoom.print_location_info()
        
    def processCommand(self,command):
        wantToQuit = False

        if(command.isUnknown()):
            print("No entiendo que queres decir")
            return False
        
        commandWord = command.getCommandWord()
        if(commandWord == "help"):
            self.printHelp()
        elif(commandWord == "go"):
            self.goRoom(command)
        elif(commandWord == "quit"):
            wantToQuit = self.quit(command)
        elif(commandWord == "look"):
            self.look_items()
        elif(commandWord == "back"):
            self.goBack()
        elif(commandWord == "take"):
            self.takeItem(command)
        elif(commandWord == "bag"):
            self.bag_items()
        elif(commandWord == "drop"):
            self.dropItem(command)
        elif(commandWord == "eat"):
            self.eat(command)
        elif(commandWord == "talk"):
            self.talk(command)    
        elif(commandWord == "open"):
            self.open(command)
        elif(commandWord == "activate"):
            self.activate(command)

        return wantToQuit

    def printHelp(self):
        print("Estas perdido. Deambulas en la empresa")
        print("Tus palabras comando son:")
        print(" go | quit | help | back | take | drop | look | bag | eat | talk | open | activate")

    def goRoom(self,command):
        if(not command.hasSecondWord()):
            print("Ir a donde?")
            return
        
        direction = command.getSecondWord()
        #nextRoom = None (esto cambia por lo de abajo)
        nextRoom = self.currentRoom.get_exit(direction)
        
        if(nextRoom == None):
            print("No hay puerta")
        else:
            self.currentRoom = nextRoom
            #Se agrega la modificacion printlocationinfo
            self.currentRoom.print_location_info()
            self.stack.push(direction)

    def goBack(self):
        direction = self.stack.pop()
        if(direction):
            nextRoom = self.currentRoom.get_exit(direction)
            if(nextRoom is None):
                print("No hay puerta")
                self.stack.inverse([direction])
            else:
                self.currentRoom = nextRoom
                self.currentRoom.print_location_info()
        else:
            print("Estas en la posicion inicial, no podes volver atras")

    # Juntar item de la habitacion 
    def takeItem(self, command):
        if(not command.hasSecondWord()):
            print("Juntar que?")
            return
        item_name = command.getSecondWord()
        item = self.currentRoom.getItem(item_name)
        if(item is None):
            print("No hay item en la habitacion con ese nombre")
        else:
            # item.picked_up es verdadero?
            if(item.picked_up):
                if(self.player.can_picked_up_item(item.weight)):
                    self.player.setItem(item)
                    self.player.print_items_information()
                
                else:
                    print("Llevas el peso maximo posible, no podes levantar el item")
                    self.currentRoom.setItem(item)
            else:
                print("Ese item no puede ser levantado")
                self.currentRoom.setItem(item)


    # Soltar item
    def dropItem(self, command):
        if(not command.hasSecondWord()):
            print("Soltar que?")
            return
        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)
        if(item is None):
            print("No tenes ese item en tu inventario")
        else:
            self.currentRoom.setItem(item)
            self.currentRoom.print_items_information()
            self.player.print_items_information()
            # Quita el peso del item del inventario del jugador 
            self.player.quitar_peso_item(item.weight)

    # Ver items en la habitacion actual
    def look_items(self):
        self.currentRoom.print_items_information()

    # Ver items en la mochila del jugador 
    def bag_items(self):
        self.player.print_items_information()
        self.player.mostrar_peso_cargado_bag()
        if(self.player.carta_en_lista() == True):
            print("Mision de la carta: juntar LlaveAntigua")

    # Comer 
    def eat(self, command):
        if(not command.hasSecondWord()):
            print("Comer que?")
            return
        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)
        if(item is None):
            print("No tenes ese item en tu inventario")
        else:
            # item.comestible es verdadero?
            if(item.snack):
                print('Has comido:', item.name)
                self.player.eliminar_peso_snack()
            # item.magico es verdadero? (Chequea si es la galleta magica)
            elif(item.magico == True):
                print("Comiste la galleta magica, tu fuerza ha aumentado a:")    
                self.player.aumentar_fuerza_galleta()
                self.player.mostrar_fuerza_max()
                self.player.eliminar_peso_galleta()
            else:
                print('Este item no es comestible')
                self.player.setItem(item)

    def talk(self, command): 
        if(not command.hasSecondWord()):
            print("Hablar con quien?")
            return

        npc_name = command.getSecondWord()
        npc = self.currentRoom.checkNpc(npc_name)

        if(npc == True):
            if(npc_name == 'yoda'):
                print("Que la fuerza te acompañe")
            elif(npc_name == 'skywalker'):
                if(self.player.llave_en_lista() == True):
                    print("Mision completada")
                else:
                    print("Aun no tienes la llave, ve a buscarla y cumple la mision")
        else: 
            print("El npc no esta en la habitacion actual")
            
    def open(self, command):
        if(not command.hasSecondWord()):
            print("Abrir que?")
            return

        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)

        if (item is None):
            print("No hay item en el inventario del jugador con ese nombre")
        else:
            if(isinstance(item, Transportador)):
                print('Habitacion guardada: ',self.currentRoom.description)
                item.room_back = self.currentRoom
            else:
                print("Este item no es del tipo transportador y no se puede abrir")

            self.player.setItem(item)

    def activate(self, command):
        if(not command.hasSecondWord()):
            print("Activar que?")
            return

        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)

        if (item is None):
            print("No hay item en el inventario del jugador con ese nombre")
        else:
            if(isinstance(item, Transportador)):
                if(item.activado()):
                    print("Transportandome")
                    self.currentRoom = item.room_back
                    print(self.currentRoom.description)
            else:
                print("Este item no es de tipo transportador y no se puede activar")
                self.player.setItem(item)


    def quit(self, command):
        if(command.hasSecondWord()):
            print("Quitar que?")
            return False
        else:
            return True

g = Game()
g.play()