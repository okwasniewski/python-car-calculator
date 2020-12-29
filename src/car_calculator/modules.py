from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, NM, HP, weight, sound, image, name, year):
        self.NM = NM
        self.HP = HP
        self.weight = weight
        self.sound = sound
        self.image = image
        self.name = name
        self.year = year

    @abstractmethod
    def GetInfo(self):
        pass

    @abstractmethod
    def SetHP(self):
        pass

    @abstractmethod
    def SetNM(self):
        pass

    @abstractmethod
    def Import(self):
        pass

    @abstractmethod
    def Export(self):
        pass

    @abstractmethod
    def PlaySound(self):
        pass

    @abstractmethod
    def GetImage(self):
        pass


# class Car1(Car):
