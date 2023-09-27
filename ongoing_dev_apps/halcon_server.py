import socket  
from time import sleep  
  
# create and configure socket on local host  
serverSocket = socket.socket()  
# host = socket.gethostname()  
host= '10.5.57.232'
port = 1026 #arbitrary port  
serverSocket.bind( ( host, port ) )  
serverSocket.listen( 1 )  
  
con, addr = serverSocket.accept()  
connected = True  
print( "connected to client" )  
  
while True:  
    try:
        # send wave to client  
        con.send( bytes( "Server wave", "UTF-8" ) )  
    
        # receive wave from client  
        # message = con.recv( 1024 ).decode( "UTF-8" )  
        message = con.recv( 1024 ) 
        print( message )  
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