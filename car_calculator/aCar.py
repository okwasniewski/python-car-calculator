from abc import ABC, abstractmethod


class aCar(ABC):
    def __init__(self, NM, HP, weight, sound, image, name, mark, year, max):
        self.NM = NM
        self.HP = HP
        self.weight = weight
        self.sound = sound
        self.image = image
        self.name = name
        self.mark = mark
        self.year = year
        self.max = max

    @property
    def NM(self):
        pass

    @NM.setter
    def NM(self, x):
        pass

    @property
    def HP(self):
        pass

    @NM.setter
    def HP(self, y):
        pass

    @property
    def weight(self):
        pass

    @property
    def name(self):
        pass

    @property
    def mark(self):
        pass

    @property
    def year(self):
        pass

    @property
    def max(self):
        pass

    @abstractmethod
    def Import(self):
        pass

    @abstractmethod
    def PlaySound(self):
        pass

    def show(self):
        pass
