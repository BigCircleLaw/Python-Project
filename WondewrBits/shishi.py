# 在屏幕上画两条线，将屏幕分为四份
from wonderguy import Display
display1 = Display()

# 在第1页以 (1, 16) 为起点， (119, 16) 为终点画一条直线
display1.draw_line(1, 16, 119, 16)

# 在第1页以 (60, 1) 为起点， (60, 32) 为终点画一条直线
display1.draw_line(60, 1, 60, 32)
