# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (501, 501)
sd.background_color = [255, 255, 0]
start_x, start_y = 0, 1
end_x, end_y = 499, 1
current_color = [0, 0, 0]
current_color_2 = [255, 0, 255]

for y in range(1, 551, 100):
    start_point = sd.get_point(start_x, y)
    end_point = sd.get_point(end_x, y)
    sd.line(start_point=start_point, end_point=end_point, color=current_color, width=4)
    for x in range(0, 599, 100):
        start_point_2 = sd.get_point(x, y)
        end_point_2 = sd.get_point(x, y + 50)
        sd.line(start_point=start_point_2, end_point=end_point_2, color=current_color, width=4)


for y in range(51, 551, 100):
    start_point = sd.get_point(start_x, y)
    end_point = sd.get_point(end_x, y)
    sd.line(start_point=start_point, end_point=end_point, color=current_color, width=4)
    for x in range(50, 499, 100):
        start_point_2 = sd.get_point(x, y)
        end_point_2 = sd.get_point(x, y + 50)
        sd.line(start_point=start_point_2, end_point=end_point_2, color=current_color, width=4)


sd.pause()