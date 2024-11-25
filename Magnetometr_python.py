import sys
import serial
from fontTools.misc.cython import returns

#definicja połączenia z portem szeregowym
with serial.Serial('COM7', 115200, timeout=1) as dev:
    #wysłanie komendy do podania danych
    dev.write(bytearray([0x03,0,0,0,0,0]))
    rxbit_all = [0]*6
    rxbit_str = ""
    i=0
    for x in range(31):
        #odczytywanie jednego bajta danych
        rx = dev.read(1)
        #konwertowanie jednego bajta danych na jego reprezentacje bitowom w formie stringa
        rxbit = bin(int.from_bytes(rx, byteorder='big'))[2:]

        #uzupełniane brakujących zer na początku
        if len(rxbit) < 8:
            for y in range(8-len(rxbit)):
                rxbit_str += "0"
            rxbit_str+=rxbit
        else:
            rxbit_str+=rxbit

        if ((x+1) % 6 == 0 or x==30):
            rxbit_all[i]= rxbit_str
            rxbit_str=''
            i+=1
if rxbit_all[5]!='00001000':
    print("Magnetometer do not reply correctly")
    sys.exit()
def magnetometer_value(z):
    val = int(rxbit_all[z][16:], 2)
    if rxbit_all[z][12] == "1":
        val = -val
    val = val / pow(10, int(rxbit_all[z][13:16], 2))
    return val
measurements = {'x': magnetometer_value(1), 'y': magnetometer_value(2), 'z':magnetometer_value(3), 'sum':magnetometer_value(4)}
print(f'x = {measurements['x']}')
print(f'y = {measurements['y']}')
print(f'z = {measurements['z']}')
print(f'sum = {measurements['sum']}')

#zapis int liczby binarnej
#decoding 2-go wiersza
#bin='10010100'
#print(int(bin,2))

#dictionary x- przypisana i zwrócona wartość przypisana wartość