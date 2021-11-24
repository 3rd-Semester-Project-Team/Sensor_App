import ParkingSensor
import time
from socket import *

serverName = '192.168.14.220'
serverPort = 10100
oldStatus = False

def send_udp_package(sensorId, occupied):
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        message = "{{'sensorId':1,'occupied':{}}}".format(occupied)
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        clientSocket.close

while True:
    newStatus = ParkingSensor.check_for_car()
    #print(newStatus)
    if newStatus != oldStatus:
        send_udp_package(1, newStatus)
        oldStatus = newStatus
        continue
    #print('sleeping')
    time.sleep(1)
    
    
    

