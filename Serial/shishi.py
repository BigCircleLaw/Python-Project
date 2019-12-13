import serial.tools.list_ports
import serial

port_list = list(serial.tools.list_ports.comports())
print(port_list)
try:
    if len(port_list) == 0:
        print('找不到串口')
        raise serial.SerialException('66')
    else:
        for str_i in port_list:
            aaa = list(str_i)
            print(str_i)
            print(aaa)
except Exception as err:
    print(Exception, type(err), err)
    print(type(str(err)), str(err))
    raise err, 
