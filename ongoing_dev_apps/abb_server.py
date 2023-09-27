import socket  
from time import sleep  
import yaml
import time
import config
from shared_memory_dict import SharedMemoryDict


# create and configure socket on local host  
serverSocket = socket.socket()  
# host = socket.gethostname()  
host = config.server_abb_ip
port = config.abb_socket_port
serverSocket.bind( ( host, port ) )  
serverSocket.listen( 1 )  
  
con, addr = serverSocket.accept()  
connected = True  
print( "connected to client" )  

# def write_to_file(msg_from_abb):
#     print("writing to yaml file")
#     ts = time.time()# getting timestamp
#     msg_to_write = {'time_stamp': [ts], 'abb_msg': [msg_from_abb]}
#     with open(r'ongoing_dev_apps/msg_from_abb.yaml', 'w') as file:
#         yaml.dump(msg_to_write, file)
#         sys.stdout.flush()
#     # file.close()

smd_config = SharedMemoryDict(name='config', size=1024)
smd = SharedMemoryDict(name='tokens', size=1024)
# smd = SharedMemoryDict(name='tokens', size=1024)



    
while True:  
    try:
        # send wave to client  
        con.send( bytes( "Server wave", "UTF-8" ) )  
    
        # receive wave from client  
        message = con.recv( 1024 ) 
        smd_config[0] = message
        # write_to_file(message)
        print( message )  

        msg_halcon_Dict = smd
        print(msg_halcon_Dict)
        
        sleep( 1 )  

    except  socket.error: 
        con, addr = serverSocket.accept()  
        print( "connection lost... reconnecting" )  
    # wait 1 second  

        while not connected:  
            # attempt to reconnect, otherwise sleep for 2 seconds  
            try:  
                con, addr = serverSocket.accept()   
                connected = True  
                print( "re-connection successful" )  
            except socket.error:  
                sleep( 2 )  
  
con.close();  