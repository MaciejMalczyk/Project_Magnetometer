import pandas as pd
import os
from datetime import datetime
from Project_Magnetometer.Magnetometr_python import *


def saveData(data, file_name):
    # Pobieranie bieżącego katalogu
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    # Tworzenie DataFrame z danych
    df = pd.DataFrame([data])

    # Zapisywanie danych do pliku CSV
    if os.path.isfile(file_path):
        # Dopisywanie danych do istniejącego pliku
        df.to_csv(file_path, mode='a', header=False, index=False, sep=";")
    else:
        # Tworzenie nowego pliku z nagłówkami
        df.to_csv(file_path, mode='w', header=True, index=False, sep=";")


start_time = round(time.time(),1)
file_name = datetime.now().strftime("%Y-%m-%d_%H;%M;%S") + '.csv'
while (time.time()-start_time<61200):
    saveData(magnetometerReadData(start_time),file_name)