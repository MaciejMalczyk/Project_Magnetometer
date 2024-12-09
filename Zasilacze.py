import os
import subprocess

def powerSupplierOn(adressIp: str):
    return subprocess.run(f'lxi scpi -a {adressIp} ":OUTP ON"', capture_output=True, text=True).stdout
def powerSupplierOff(adressIp: str):
    return subprocess.run(f'lxi scpi -a {adressIp} ":OUTP OFF"', capture_output=True, text=True).stdout
def powerSupplierIfOn(adressIp: str):
    if subprocess.run(f'lxi scpi -a {adressIp} ":OUTP?"', capture_output=True, text=True).stdout=='ON\n':
        return True
    else: return False
def powerSupplierMeasurementVoltage(adressIp: str):
    return float(subprocess.run(f'lxi scpi -a {adressIp} ":MEAS:VOLT?"', capture_output=True, text=True).stdout)
def powerSupplierMeasurementAll(adressIp: str):
    return str(subprocess.run(f'lxi scpi -a {adressIp} ":MEAS:ALL?"', capture_output=True, text=True).stdout)
print(powerSupplierIfOn("192.168.88.201"))




#print(powerSupplierMeasurementVoltage("192.168.88.201"))


