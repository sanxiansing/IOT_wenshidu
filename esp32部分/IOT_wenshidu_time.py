import machine
from time import sleep
import network
from machine import RTC
import socket
import ntptime
import time
def get_time():
    while True:   #时间校准
        try:
            print('time ing')
            ntptime.settime()
            print('time ok')
            break;
        except:
            print('time no')
            time.sleep(1)
    mytime=time.localtime()
    mytime='%d-%d-%d %d:%d:%d'%(mytime[0],mytime[1],mytime[2],mytime[3]+8,mytime[4],mytime[5])

    print(mytime)
    return mytime
def dht(dhPin):
    import dht
    d = dht.DHT11(machine.Pin(dhPin))
    while True:
        d.measure()
    #     temp = d.temperature() # eg. 23 (°C)
    #     RH = d.humidity()    # eg. 41 (% RH)
    #     data = "temp(f): %s humidity: %s" % (32.0 + 1.8*d.temperature(), d.humidity())
        data = "temp(c): %s℃ humidity: %sRH" % (d.temperature(), d.humidity())
        result=[d.temperature(),d.humidity()]
        print(data)
        return result
def do_connect_wifi():

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('WiFi名称', 'WiFi密码')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
def do_connect_server():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockaddr = socket.getaddrinfo('服务器ip/域名', 端口号)[0][-1]
    client.connect(sockaddr)
    return client
def sendData(data,sock):
    now=get_time()
    s_data=[{'temperature':data[0],'humidity':data[1],'time':now}]
    print('ToSendData: ',s_data)
    data_send = bytes(str(s_data), 'utf-8')
    sock.send(data_send)
    data = sock.recv(1024)
    station_replay=str(data,'utf-8')
    print('Server response: ',station_replay)
    
if __name__=="__main__":
    try:
        do_connect_wifi()
        client=do_connect_server()
        data=[]
        while(1):
            data=dht(2)
            sendData(data,client)
            sleep(30)
    except KeyboardInterrupt:
        client.send('stop')
        client.close()