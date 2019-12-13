import serial
import sys
import time
import serial.tools.list_ports

def
port_list = list(serial.tools.list_ports.comports())

port_str = []
if len(port_list) == 0:
    print('找不到串口')
else:
    for str_i in port_list:
        port_str = list(str_i)
        id_str = port_str[1].split(' ')
        if 'CH340' in id_str:
            print('找到串口：' + str(str_i))
            port_str.append(str(str_i))
            break
        port_str = []
        
if not len(port_str[3]):
    print('没有连接豌豆拼！！！')
    sys.exit(0)
print(port_str)
# try:
#     ser = serial.Serial(port_str[0], 9600, timeout=1)
# except serial.SerialException:
#     print('无法正常打开串口！！！')
#     sys.exit(0)
    
# timeCount = 0
# while not ser.isOpen():
#     ser.open()
#     time.sleep(0.1)
#     timeCount += 1
#     if timeCount > 30:
#         print('连接失败:' + port_str[3])
# print(ser)
# print('串口打开成功！！！')
# ser.close()
