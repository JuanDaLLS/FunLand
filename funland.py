from abc import ABC, abstractmethod
class atracciones(ABC):
    @abstractmethod
    def _init_(self, capacidad, duracion, nombre, estado):
        self.__capacidad = capacidad
        self.__duracion = duracion
        self.__nombre = nombre
        self.__estado = estado
class montana_rusa(atracciones):
    def _init_(self, capacidad, durcion, nombre, altura_maxima, velocidad_maxima):
        super()._init_(capacidad, durcion, nombre)
        self.__altura_maxima = altura_maxima
        self.__velocidad_maxima = velocidad_maxima
    def mostrar_info(self):
        return f"Montaña Rusa: {self._nombre}, Capacidad: {self.capacidad}, Duración: {self.duracion} min, Altura Máxima: {self.altura_maxima} m, Velocidad Máxima: {self.velocidad_maxima} km/h estado: {self._estado}"

class tobogan_agua(atracciones):
    def _init_(self, capacidad, duracion, nombre, longitud, inclinacion):
        super()._init_(capacidad, duracion, nombre)
        self.__longitud = longitud
        self.__inclinacion = inclinacion
    def mostrar_info(self):
        return f"Tobogán de Agua: {self._nombre}, Capacidad: {self.capacidad}, Duración: {self.duracion} min, Longitud: {self.longitud} m, Inclinación: {self.inclinacion}° estado: {self._estado}"
class casa_sustos(atracciones):
    def _init_(self, capacidad, duracion, nombre, numero_habitaciones, nivel_sustos):
        super()._init_(capacidad, duracion, nombre)
        self.__numero_habitaciones = numero_habitaciones
        self.__nivel_sustos = nivel_sustos
    def mostrar_info(self):
        return f"Casa de Sustos: {self._nombre}, Capacidad: {self.capacidad}, Duración: {self.duracion} min, Número de Habitaciones: {self.numero_habitaciones}, Nivel de Sustos: {self.nivel_sustos} estado: {self._estado}"