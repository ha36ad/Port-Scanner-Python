import socket
import sys
from datetime import datetime

#Ask user for a server
server = raw_input("Enter a scan location: ")

#Scanner function
def Port_scanner (port):
    #Declare socket kind and family
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: #If scanner sucessfully connects, return true (port is open)
        sock.connect((server,port))
        return True
    #If keyboard is pressed
    except KeyboardInterrupt:
        sys.exit()

    except:
        return False #Port is not open

#Time scanner started
time = datetime.now()

#For loop for scanning
for port in range (1,28):
    if Port_scanner(port):
        print ("Port ", port , " is open")
    else:
        print ("Port ", port ," is closed")
