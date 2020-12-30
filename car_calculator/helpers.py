import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from Car import Car

BMW = Car(500, 500, 500, "../static/m5.jpg", "M5",
          "BMW", 2017, 295, "../static/m5.mp3")

Audi = Car(500, 500, 500, "../static/rs7.jpg", "RS7",
           "Audi", 2017, 295, "../static/rs7.mp3")

Mercedes = Car(500, 500, 500, "../static/w222.jpg", "W222",
               "Mercedes", 2017, 295, "../static/w222.mp3")


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


quarter_plot(2000, 520, 1800, 324, 2100, 650)
