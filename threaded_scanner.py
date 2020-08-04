import threading
import socket
from queue import Queue

#Ask user for an IP address
server = raw_input("Enter a scan location: ")

#Call queue
queue = Queue()

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


#Define worker function
def worker():
    while True:
        #Ask queue for worker
        queue.get()
        
        #Run the worker using scanner function's results
        Port_scanner(worker)

        queue.task_done()

#Initalize thread array
thread_list = []

#For loop for running the scanner
for i in range (1,1025):
    Threader = threading.Thread(target=worker)
    thread_list.append(Threader)

for Threader in thread_list:
    Threader.start()

for Threader in thread_list:
    Threader.join()

