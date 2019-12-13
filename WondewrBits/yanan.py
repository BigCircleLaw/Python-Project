from wonderbits import *
# # import wonderbits
import time

d1 = Display()
p1 = Pulse()
h1 = Hall()
c1 = Control()
# #
time.sleep(3)
# #
# content = 1
# for i in range(100):
#     d1.print(1, 1, content)
#     content += 1
import math

# d1.turn_to_page(3)
# time.sleep(2)
# d1.turn_to_page(2)
s1 = Signal()
print(time.time_ns() / 1000000000)
# s1.play_a_note(600, 2000)
# print(time.time_ns() / 1000000000)
# time.sleep(10)
h1.calibrate()
# print(time.time_ns() / 1000000000)
# value = p1.get_heart_rate()
d1.print(1, 1, c1.is_sw1_pressed())
