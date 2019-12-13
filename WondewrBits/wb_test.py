# 绘制脉搏波形
from wonderbits import Pulse, Display


display1 = Display()
pulse1 = Pulse()

x = 0
while True:
    if pulse1.get_unread_wave_count():
        x = x + 1
        y = pulse1.get_heart_wave()/8
        display1.draw_chart(x, y)

    if x >= 120:
        x = 0
        display1.clear_all_pages()
