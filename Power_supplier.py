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
def powerSupplierRange(adressIp: str):
    return subprocess.run(f'lxi scpi -a {adressIp} ":OUTP:RANG P20V"', capture_output=True, text=True).stdout
def powerSupplierSetVoltage(adressIp: str, Voltage: float):
    return subprocess.run(f'lxi scpi -a {adressIp} ":VOLT {Voltage}"', capture_output=True, text=True).stdout