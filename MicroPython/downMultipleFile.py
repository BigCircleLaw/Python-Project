import serial
import serial.tools.list_ports
import os
import threading

def get_serial_ports_list():
    can_used_serial_port = list()
    port_list = list(serial.tools.list_ports.comports())
    for i in range(len(port_list)):
        port = port_list[i]
        if (port.pid == 0x7523
                and port.vid == 0x1A86) or (port.pid == 60000
                                            and port.vid == 0x10C4):
            can_used_serial_port.append(port.device)
    return can_used_serial_port

serial_list = get_serial_ports_list()

print (serial_list)


def download(port):
    os.system('esptool.py --chip esp32 --port ' + port +' write_flash -z 0x1000 wonderbits-0.2.3.bin')


for port in serial_list:
    threading.Thread(target=download,args=(port, )).start()
