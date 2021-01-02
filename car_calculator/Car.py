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
            self.__NM = x
        else:
            print("Out of range!")

    @property
    def HP(self):
        return self.__HP

    @HP.setter
    def HP(self, y):
        if 1 < y < 1000:
            self.__HP = y
        else:
            print("Out of range!")

    @property
    def weight(self):
        return self.__weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = str(value)

    @property
    def mark(self):
        return self.__mark

    @property
    def year(self):
        return self.__year

    @property
    def max(self):
        return self.__max

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = str(value)

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, value):
        self.__sound = value

    def quarter_mile(self):
        et = float(6.290*(self.__weight*2.20462262/self.__HP)**(1/3))  # czas
        mph = float(224*(self.__HP*0.745699872/self.__weight)
                    ** (1/3))  # w milach
        result = float(mph*1.6)  # w km/h
        return result, et

    def export_quarter_mile(self, fileName):
        result, et = self.quarter_mile()
        f = open(str(fileName), 'w+')
        f.write("Czas 1/4 mili: ")
        f.write(str(et))
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

    def StopSound(self):
        pygame.mixer.music.stop()

    def top_speed(self):
        distance = float(0.25*1.6)  # TO DO

    def show(self):
        return "Marka: %s Model: %s Rocznik: %d HP: %d NM: %d Weight: %d ".format(self.mark(), self.__name(), self.__year(), self.__HP(), self.__NM(), self.__weight())


def quarter_plot(firstw, firsthp, secondw, secondhp, thirdw, thirdhp):
    x = np.linspace(0, 300, 1)
    point0 = [0, 6.269 * (firstw / firsthp)**(1/3)]
    point1 = [0, 250]
    point2 = [0, 6.269 * (secondw / secondhp)**(1/3)]
    point3 = [0, 250]
    point4 = [0, 6.269 * (thirdw / thirdhp)**(1/3)]
    point5 = [0, 250]

    # wykres do point, to czas w jakim pokona 1/4 mili

    plt.title('1/4 MILE')
    # plt.plot(x, point1, 'r', x, point2, 'grey', x, point3, 'k')
    # plt.plot(point0, point1, 'r', point0, point2, 'grey', point0, point3, 'k')
    plt.plot(point0, point1)
    plt.plot(point2, point3)
    plt.plot(point4, point5)
    plt.grid(True)

    plt.xlabel('Time (s)')
    plt.xticks([0, 2, 4, 6, 8, 10, 12])

    plt.ylabel('Distance (mile)')
    plt.yticks([0, 50, 100, 150, 200, 250])

    red = mpatches.Patch(color='red', label='Audi RS7')
    green = mpatches.Patch(color='green', label='BMW M5')
    blue = mpatches.Patch(color='blue', label='Mercedes W222')
    plt.legend(handles=[red, green, blue], loc='upper center',
               bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=1)

    plt.show()
