# -*- coding: utf-8 -*-

import simple_draw as sd

from random import randint

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# point = sd.get_point(300, 300)
# radius = 59
# for _ in range(3):
#     sd.circle(center_position=point,radius=radius, width=2)
#     radius += 5


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, color=sd.random_color(), width=2)
        radius += step

# point = sd.get_point(300, 300)
# step = 5
# bubble(point, step)

# Нарисовать 10 пузырьков в ряд
# step = 5
# for x in range(80, 981, 100):
#     point = sd.get_point(x, 300)
#     bubble(point, step)

# Нарисовать три ряда по 10 пузырьков
# step = 5
# for y in range(80, 301, 100):
#     for x in range(80, 981, 100):
#         point = sd.get_point(x, y)
#         bubble(point, step)



# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = randint(3, 15)
    bubble(point, step)

sd.pause()


