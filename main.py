from Project_Magnetometer.Magnetometr_python import magnetometerReadData
from Project_Magnetometer.Power_supplier import powerSupplierOn, powerSupplierMeasurementVoltage, \
    powerSupplierSetVoltage
import time

# x - big, z - small, y - medium
IpPowerSupplier={"big":"192.168.88.202", "medium":"192.168.88.203", "small":"192.168.88.201"}
powerSupplierOn(IpPowerSupplier["big"])
powerSupplierOn(IpPowerSupplier["medium"])
powerSupplierOn(IpPowerSupplier["small"])
interval=0.5

while True:
    res = magnetometerReadData(0)
    x_d = 0-res["x"]
    y_d = 0-res["y"]
    z_d = 0-res["z"]
    x_v = powerSupplierMeasurementVoltage(IpPowerSupplier["big"])
    y_v = powerSupplierMeasurementVoltage(IpPowerSupplier["medium"])
    z_v = powerSupplierMeasurementVoltage(IpPowerSupplier["small"])

    print(x_d, y_d, z_d)
    if (x_d < - interval):
        powerSupplierSetVoltage(IpPowerSupplier["big"], x_v - x_d*0.002)

    if (x_d > interval):
        powerSupplierSetVoltage(IpPowerSupplier["big"], x_v - x_d * 0.002)

    # print(f"z_d: {y_d}, z_v: {y_v}")
    if (y_d < - interval):
        powerSupplierSetVoltage(IpPowerSupplier["medium"], y_v + y_d * 0.002)
        # print(f"S: {y_v + y_d * 0.002}")

    if (y_d > interval):
        powerSupplierSetVoltage(IpPowerSupplier["medium"], y_v + y_d * 0.002)
        # print(f"S: {y_v + y_d * 0.002}")

    # print(f"z_d: {z_d}, z_v: {z_v}")
    if (z_d < - interval):
        powerSupplierSetVoltage(IpPowerSupplier["small"], z_v + z_d * 0.002)
        # print(f"S: {z_v - z_d * 0.002}")

    if (z_d > interval):
        powerSupplierSetVoltage(IpPowerSupplier["small"], z_v + z_d * 0.002)
        # print(f"S: {z_v - z_d * 0.002}")

