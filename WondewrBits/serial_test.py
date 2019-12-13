import serial
import time
from threading import Thread

ser = serial.Serial('COM18', 115200)


start = 0.0
def waiting_for_response():
    while True:
        while ser.inWaiting():
            print('-'*20)            
            print('start recving:',(time.time() - start)*1000)
            buf = b''
            while ser.inWaiting():
                buf += ser.read(1)
                i = 0.2*1231

            print('recved:',(time.time() - start)*1000)
            print(buf)
            print('-'*20)
Thread(target=waiting_for_response ).start()

print(ser.name)
time.sleep(2)

start = time.time()
ser.write(b'display1.print(1,1,123)\r\n')
time.sleep(1)
start = time.time()
ser.write(b'display1.print(1,1,123)\r\n')
time.sleep(1)
start = time.time()
ser.write(b'display1.print(1,1,123)\r\n')
time.sleep(1)
start = time.time()
ser.write(b'display1.print(1,1,123)\r\n')


# ser.write(b'\x01')
# time.sleep(1)
# start = time.time()
# ser.write(b'display1.print(1,1,456)'+b'\x04')
# time.sleep(1)
# start = time.time()
# ser.write(b'display1.print(1,1,789)'+b'\x04')
