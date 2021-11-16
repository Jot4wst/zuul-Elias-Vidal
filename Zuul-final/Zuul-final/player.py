class Player(): 
    def __init__(self, name, max_weight, peso_llevado):
        self.name = name
        self.max_weight = max_weight
        self.items = {}
        # Peso que el jugador lleva cargando los items
        self.peso_llevado = peso_llevado
        
    def setItem(self, item):
        self.items[item.name] = item

    # Ver items que lleva el jugador
    def print_items_information(self):
        print("Items que llevas cargando: ")
        items = '| '
        for item in self.items.keys():
            items += self.items[item].name + ' | '
        print(items)
        if(self.carta_en_lista() == True):
            print("Mision de la carta: juntar LlaveAntigua")

# GetItem quita de la mochila el item seleccionado
    def getItem(self, item):
        if(item in self.items):
            return self.items.pop(item)
        else:
            return None

    # Pregunta si se puede juntar el item debido al peso que llevamos
    # Devuelve verdadero o falso y muestra el peso restante que se puede juntar
    def can_picked_up_item(self, weight):
        peso_total = 0
        for item in self.items.values():
            peso_total=peso_total+item.weight
        peso_total = peso_total+weight
        self.peso_llevado = peso_total
        return peso_total <= self.max_weight
        
    # Aumentar la fuerza del jugador al comer la galleta magica
    def aumentar_fuerza_galleta(self):
        self.max_weight = self.max_weight+7
        return
    
    # Mostrar la capacidad maxima que se puede cargar 
    def mostrar_fuerza_max(self):
        print(self.max_weight)
        return

    # Muestra el peso llevado por el jugador en el inventario  
    def mostrar_peso_cargado_bag(self):
        peso_cargado = round(self.peso_llevado,1)
        peso_restante = self.max_weight-peso_cargado
        peso_restante_trunc = round(peso_restante,1) 
        print("Llevas cargando este peso:", peso_cargado)
        print("Capacidad restante que podes juntar:", peso_restante_trunc)

    # Quita el peso del item actual (drop)
    def quitar_peso_item(self, peso):
        self.peso_llevado = self.peso_llevado-peso
        return

    # Quita el peso de la galleta del inventario 
    def eliminar_peso_galleta(self):
        self.peso_llevado = self.peso_llevado - 0.1
    
    # Quita el peso del snack del inventario 
    def eliminar_peso_snack(self):
        self.peso_llevado = self.peso_llevado - 0.2
    
    def carta_en_lista(self):
        if ("carta" in self.items):
            return True
        else:
            return False
    
    def llave_en_lista(self):
        if ("LlaveAntigua" in self.items):
            return True
        else:
            return False