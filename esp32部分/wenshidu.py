import dht
import machine
from time import sleep

d = dht.DHT11(machine.Pin(2))

while True:
    d.measure()
#     temp = d.temperature() # eg. 23 (°C)
#     RH = d.humidity()    # eg. 41 (% RH)
#     data = "temp(f): %s humidity: %s" % (32.0 + 1.8*d.temperature(), d.humidity())
    data = "temp(c): %s℃ humidity: %sRH" % (d.temperature(), d.humidity())
    print(data)
    sleep(1)
