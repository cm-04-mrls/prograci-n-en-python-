class jugador :
   # constructor
    def __init__(self, dor, nom) :
      self.dorsal = dor
      self.nombre = nom
    def mostrar(self) :
      print(f'{self.dorsal}.{self.nombre}') 

#programa principal
jugador1 = jugador (10, "Pau Gasol") 
jugador2 = jugador (47, "Marc Marquez") 

jugador1.mostrar()
jugador2.mostrar()