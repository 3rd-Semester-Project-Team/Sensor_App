import ParkingSensor
import time
from socket import *

serverName = '192.168.14.220'
serverPort = 10100
oldStatus = False

def send_udp_package(sensorId, occupied):
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        message = '{{"sensorId":1,"occupied":{}}}'.format(occupied)
        clientSocket.sendto(message.encode(),('<broadcast>', serverPort))
        clientSocket.close

while True:
    newStatus = ParkingSensor.check_for_car()
    #print(newStatus)
    message = "false"
    if newStatus != oldStatus:
        if newStatus:
			message = "true"
        else:
			message = "false"
        send_udp_package(1, message)
        oldStatus = newStatus
        continue
    #print('sleeping')
    time.sleep(1)
    
    
    

