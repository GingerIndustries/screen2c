import screen2c
import psutil
from time import sleep, strftime
import sys


mylcd = screen2c.Display(0x27)
mylcd.setCursor(screen2c.CursorMode.NONE)
ver = ""
for x in range(0, 3):
    ver += str(sys.version_info[x])
    if x != 2:
        ver += "."
while True:
    mylcd.clear()
    mylcd.write(strftime("%b %d %I:%M:%S %p"), 1)
    mylcd.write("CPU: " + str(round(psutil.cpu_percent())) + "% " + str(round(psutil.sensors_temperatures(True)["cpu_thermal"][0].current)) + "F", 2)
    sleep(0.9)