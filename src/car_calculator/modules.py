from abc import ABC, abstractmethod
import importlib
from playsound import playsound


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
        return self.__NM

    @NM.setter
    def NM(self, x):
        if 1 < x < 1000:
            self.NM(x)
        else:
            print("Out of range!")

    @property
    def HP(self):
        return self.__HP

    @NM.setter
    def HP(self, y):
        if 1 < y < 1000:
            self._HP_setter(y)
        else:
            print("Out of range!")

    @property
    def weight(self):
        return self.__weight

    @property
    def name(self):
        return self.__name

    @property
    def mark(self):
        return self.__mark

    @property
    def year(self):
        return self.__year

    @property
    def max(self):
        return self.__max

    @abstractmethod
    def Import(self):
        pass

    @abstractmethod
    def Export(self):
        pass

    @abstractmethod
    def PlaySound(self):
        pass

    def print(self):
        print('Model: ', self.__mark(), self.__name(), '\n Year: ', self.__year(
        ), '\n Horse Power: ', self.__HP(), '\n NM: ', self.__NM(), '\n Weight ', self.__weight())


class Car(aCar):
    def __init__(self, NM, HP, weight, image, name, mark, year, max, sound):
        self.__NM = NM
        self.__HP = HP
        self.__weight = weight
        self.__image = image
        self.__sound = sound
        self.__name = name
        self.__mark = mark
        self.__year = year
        self.__max = max

    def quarter_mile(self):
        et = float(6.290*(self.__weight/self.__HP)**(1/3))  # czas
        mph = float(224*(self.__HP/self.__weight)**1/3)  # w milach
        result = float(mph*1.6)  # w km/h

        print('1/4 Mile Elapsed Time: ', et)
        print('1/4 Mile Trap Speed: ', result)

        f = open('result.txt', 'r+')
        f.write('result.txt')
        f.close()

    def Import(self):
        f = open('filename.txt', 'r+')
        f.writelines('filename.txt')
        f.close()

    def Export(self):
        f = open('result.txt', 'r+')
        f.write('result.txt')
        f.close()

    def PlaySound(self):
        playsound(self.__sound)

    def top_speed(self):
        distance = float(0.25*1.6)  # TO DO


ob1 = Car(500, 500, 500, "../static/rs7.jpg", "rs7",
          "audi", 2017, 295, "../static/rs7.mp3")
ob1.PlaySound()
