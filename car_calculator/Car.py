import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from playsound import playsound
import pygame
import time
from aCar import aCar


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

    def quarter_mile(self):
        et = float(6.290*(self.__weight*2.20462262/self.__HP)**(1/3))  # czas
        mph = float(224*(self.__HP*0.745699872/self.__weight)
                    ** (1/3))  # w milach
        result = float(mph*1.6)  # w km/h

        print('1/4 Mile Elapsed Time[s]:  ', et)
        print('1/4 Mile Trap Speed[km/h]: ', result)

        f = open('result.txt', 'w+')
        f.write("Czas 1/4 mili: ")
        f.write(str(et))
        f.write("\nPredkosc[mile]:")
        f.write(str(mph))
        f.write("\nPredkosc[hm/h]:")
        f.write(str(result))
        f.close()

    def Import(self):
        f = open('filename.txt', 'r+')
        f.writelines('filename.txt')
        f.close()

    def PlaySound(self):
        pygame.init()
        pygame.mixer.music.load(self.__sound)
        pygame.mixer.music.play()
        time.sleep(10)

    def StopSound(self):
        pygame.mixer.music.stop()

    def top_speed(self):
        distance = float(0.25*1.6)  # TO DO

    def show(self):
        return "Marka: %s Model: %s Rocznik: %d HP: %d NM: %d Weight: %d " % (self.mark(), self.__name(), self.__year(), self.__HP(), self.__NM(), self.__weight())


BMW = Car(750, 625, 2000, "../static/m5.jpg", "M5",
          "BMW", 2017, 295, "../static/m5.mp3")

Audi = Car(500, 500, 500, "../static/rs7.jpg", "RS7",
           "Audi", 2017, 295, "../static/rs7.mp3")

Mercedes = Car(500, 500, 500, "../static/w222.jpg", "W222",
               "Mercedes", 2017, 295, "../static/w222.mp3")

BMW.quarter_mile()
