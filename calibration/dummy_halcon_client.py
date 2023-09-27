import socket  
from time import sleep  
import config
  
# configure socket and connect to server  
clientSocket = socket.socket()  
# host = socket.gethostname()  
host = config.server_halcon_ip
port =  config.halcon_socket_port
clientSocket.connect( ( host, port ) )  
  
# keep track of connection status  
connected = True  
print( "connected to server" )  

n = -2
while True:  

    # attempt to send and receive wave, otherwise reconnect  
    try:
        # print (n)
        if n == -2:
            clientSocket.send( bytes( "Ball", "UTF-8" ) )
            print ("sent msg :Ball")
            # print("listening.. ")
            # print ("msg received: " + clientSocket.recv( 1024 ).decode( "UTF-8" )  )
            n+=1
            print(n)
        elif n == -1:   
            clientSocket.send( bytes( "Home", "UTF-8" ) )
            print ("sent msg: Home")
            # print ("msg received: " + clientSocket.recv( 1024 ).decode( "UTF-8" )  )
            n+=1  
            print(n)
        elif n == 0:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            print("listening.. ")
            print (clientSocket.recv( 1024 ).decode( "UTF-8" )  )
            clientSocket.send( bytes( "get_pos", "UTF-8" ) )
            print ("sent msg: get_pose")
            # print ("msg received: " + clientSocket.recv( 1024 ).decode( "UTF-8" )  )
            n+=1
            print(n)
        elif n == 1:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            print("listening.. ")
            print (clientSocket.recv( 1024 ).decode( "UTF-8" )  )
            clientSocket.send( bytes( "get_pos", "UTF-8" ) )
            print ("sent msg: get_pose")
            # print ("msg received: " + clientSocket.recv( 1024 ).decode( "UTF-8" )  )
            n+=1
            print(n)
        elif n == 2:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 3:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 4:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 5:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 6:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 7:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 8:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 9:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 10:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 11:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 12:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 13:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 2:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 14:   
            clientSocket.send( bytes( "CaliPos_"+ str(n), "UTF-8" ) )
            print ("CaliPos_"+ str(n))
            n+=1
            print(n)
        elif n == 2:   
            print (n)
            print ("DONE")



        else:
            print ("else triggred")

        print("listening.. ")
        print ("received msg " + clientSocket.recv( 1024 ).decode( "UTF-8" )  )
        clientSocket.send( bytes( "ok", "UTF-8" ) )

    except socket.error:
        # set connection status and recreate socket  
        connected = False  
        clientSocket = socket.socket()  
        print( "connection lost... reconnecting" )  
        while not connected:  
            # attempt to reconnect, otherwise sleep for 2 seconds  
            try:  
                clientSocket.connect( ( host, port ) )  
                connected = True  
                print( "re-connection successful" )  
            except socket.error:  
                sleep( 2 )  
    sleep(1)
  
clientSocket.close(); 