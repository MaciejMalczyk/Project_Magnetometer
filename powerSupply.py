import subprocess
import sys

def powerSupplyOn(adressIp: str):
    res = subprocess.run(["lxi",  "scpi", "-a", adressIp, ":OUTP ON"], capture_output=True, text=True)
    if res.stderr:
        print(res.stderr)
        sys.exit(0)
    else:
        return res.stdout


def powerSupplyOff(adressIp: str):
    res = subprocess.run(["lxi", "scpi", "-a", adressIp, ":OUTP OFF"], capture_output=True, text=True)
    if res.stderr:
        print(res.stderr)
        sys.exit(0)
    else:
        return res.stdout

def powerSupplyIfOn(adressIp: str):
    res = subprocess.run(["lxi", "scpi", "-a", adressIp, ":OUTP?"], capture_output=True, text=True)
    if res.stderr:
        print(res.stderr)
        sys.exit(0)
    else:
        if res.stdout == 'ON\n':
            return True
        else:
            return False

def powerSupplyMeasurementVoltage(adressIp: str):
    res = subprocess.run(["lxi", "scpi", "-a", adressIp, ":MEAS:VOLT?"], capture_output=True, text=True)
    if res.stderr:
        print(res.stderr)
        sys.exit(0)
    else:
        return float(res.stdout)


def powerSupplyMeasurementAll(adressIp: str):
    res = subprocess.run(["lxi", "scpi", "-a", adressIp, ":MEAS:ALL?"], capture_output=True, text=True)
    if res.stderr:
        print(res.stderr)
        sys.exit(0)
    else:
        return str(res.stdout)

def powerSupplyRange(adressIp: str):
    res = subprocess.run(["lxi", "scpi", "-a", adressIp, ":OUTP:RANG P20V"], capture_output=True, text=True)
    if res.stderr:
        print(res.stderr)
        sys.exit(0)
    else:
        return res.stdout

def powerSupplySetVoltage(adressIp: str, voltage: float):
    res = subprocess.run(["lxi", "scpi", "-a", adressIp , f':VOLT {voltage}'], capture_output=True, text=True)
    if res.stderr:
        print(res.stderr)
        sys.exit(0)
    else:
        return res.stdout
