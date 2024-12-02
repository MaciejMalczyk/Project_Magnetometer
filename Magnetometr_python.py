import sys
from webbrowser import Error

import serial
from fontTools.misc.cython import returns
# algorytmy: Levenberg Marquat,
#definicja połączenia z portem szeregowym
def fun():
    try:
        with serial.Serial('COM7', 115200, timeout=1) as dev:
            #wysłanie komendy do podania danych
            dev.write(bytearray([0x03,0,0,0,0,0]))
            rxbit_aliases = ["x", "y", "z", "s"]
            rxbit_str = ["","","","","",""]
            res = dict(x=0, y=0, z=0, s=0)
            i=0
            for x in range(31):
                #odczytywanie jednego bajta danych
                rx = dev.read(1)
                #konwertowanie jednego bajta danych na jego reprezentacje bitową w formie stringa
                rxbit = bin(int.from_bytes(rx, byteorder='big'))[2:]

                #uzupełniane brakujących zer na początku
                if len(rxbit) < 8:
                    for y in range(8-len(rxbit)):
                        rxbit_str[i] += "0"
                    rxbit_str[i] += rxbit
                else:
                    rxbit_str[i] += rxbit

                if ((x+1) % 6 == 0):
                    if not ((x+1)/6 == 1):
                        if rxbit_str[i][12] == "1":
                            res[rxbit_aliases[i-1]] = -1 * int(rxbit_str[i][16:], 2) / pow(10, int(rxbit_str[i][13:16], 2))
                        else:
                            res[rxbit_aliases[i-1]] = int(rxbit_str[i][16:], 2) / pow(10, int(rxbit_str[i][13:16], 2))
                    i+=1
        # return measurements
        return res
    # exception handler
    except Exception as e:
        print("Error occured: ",e)
        return 0



print(fun())
