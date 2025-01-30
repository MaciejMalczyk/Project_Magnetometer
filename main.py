from magnetometer import Magnetometer
from powerSupply import powerSupplyOn, powerSupplyMeasurementVoltage, powerSupplySetVoltage

# x - big, z - small, y - medium
powerSupplyIp={"big":"192.168.88.202", "medium":"192.168.88.203", "small":"192.168.88.201"}

powerSupplyOn(powerSupplyIp["big"])
powerSupplyOn(powerSupplyIp["medium"])
powerSupplyOn(powerSupplyIp["small"])

interval=0.2
multiplier=0.01

magnetometer = Magnetometer("/dev/ttyUSB0")

while True:

    # This is correct for fixed orientation. Modify >, < and - symbols for other orientations.
    res = magnetometer.readData()
    x_d = 0-res["x"]
    y_d = 0-res["y"]
    z_d = 0-res["z"]
    x_v = powerSupplyMeasurementVoltage(powerSupplyIp["big"])
    y_v = powerSupplyMeasurementVoltage(powerSupplyIp["medium"])
    z_v = powerSupplyMeasurementVoltage(powerSupplyIp["small"])

    if (x_d < - interval):
        powerSupplySetVoltage(powerSupplyIp["big"], x_v - x_d * multiplier)

    if (x_d > interval):
        powerSupplySetVoltage(powerSupplyIp["big"], x_v - x_d * multiplier)

    if (y_d < - interval):
        powerSupplySetVoltage(powerSupplyIp["medium"], y_v + y_d * multiplier)

    if (y_d > interval):
        powerSupplySetVoltage(powerSupplyIp["medium"], y_v + y_d * multiplier)

    if (z_d < - interval):
        powerSupplySetVoltage(powerSupplyIp["small"], z_v + z_d * multiplier)

    if (z_d > interval):
        powerSupplySetVoltage(powerSupplyIp["small"], z_v + z_d * multiplier)


