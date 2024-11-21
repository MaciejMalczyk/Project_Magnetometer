import serial

#definicja połączenia z portem szeregowym
with serial.Serial('COM3', 115200, timeout=1) as dev:
    #wysłanie komendy do podania danych
    dev.write(bytearray([0x03,0,0,0,0,0]))

    for x in range(31):
        rxbit_str = ""
        #odczytywanie jednego bajta danych
        rx = dev.read(1)
        #konwertowanie jednego bajta danych na jego reprezentacje bitowom w formie stringa
        rxbit = bin(int.from_bytes(rx, byteorder='big'))[2:]

        #uzupełniane brakujących zer na początku
        if len(rxbit) < 8:
            for y in range(8-len(rxbit)):
                rxbit_str += "0"
            rxbit_str += rxbit
        else:
            rxbit_str = rxbit

        if (x)%6 == 0:
            print("------")

        print(rxbit_str)

#zapis int liczby binarnej
#decoding 2-go wiersza
#bin='10010100'
#print(int(bin,2))

#dictionary x- przypisana i zwrócona wartość przypisana wartość
