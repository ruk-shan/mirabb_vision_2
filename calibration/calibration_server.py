import socket  
from time import sleep
import config 
import json
from getkey import getkey, key
  
# create and configure socket on local host  
serverSocket = socket.socket()   
host = config.server_halcon_ip
port =  config.halcon_socket_port

serverSocket.bind( ( host, port ) )  
serverSocket.listen( 1 )  
  
con, addr = serverSocket.accept()  
connected = True  
print( "connected to client" )


# send_message = ''
recv_message = 'YY'
CaliPos = -1

#send robot pos to halcon
def get_robot_pos(line):
    print ("---------------")
    print (line)
    count = 1
    while True:
        try:
            f = open("calibration/robot_pos.txt", "r")
            file  = f.read()
            file  = f.close()
            json_object = json.loads(file)
            val_to_return = json_object[str(line)]  
            return val_to_return
        except:
            count += 1
            if count > 10:
                print ("unable to read 'robot_pos.txt'")
                break

def move_robot_to_pos(pos):
    print("Press enter after the robot moved to pos_" + str(pos))
    while True:
    # Get the pressed key
        var = getkey()
    # Print the pressed key
        print(var)
        if var == key.ENTER:
        # If the ENTER key is pressed, break the While loop.
            print("You pressed enter, Hope the robot is at pos_" + str(pos))
            break  
    return True


while True:  
    try:

        #resposing to recv_messages
        if (recv_message == 'Ball'):
            print ('received Ball')
            con.send( bytes("ok","UTF-8" ) ) 
            print ('sent msg : ok')

        elif (recv_message == 'get_pos'):
            send_message = str(get_robot_pos(CaliPos))
            print ("received 'get_pos  '+send_message")

            print(f'sending message....:{send_message}')
            con.send( bytes(send_message, "UTF-8" ) ) 

        elif (recv_message == 'Home'):
            send_message = "ok"
            print ("received 'home'")
            con.send( bytes("ok, moved to home.", "UTF-8" ) ) 
        
        elif (CaliPos >-1):
            print ("received CaliPos"+ str(CaliPos))
            move_robot_to_pos(CaliPos)
            con.send( bytes("ok, moved to CaliPos_"+ str(CaliPos), "UTF-8" ) ) 
        
        else:
            send_message = "ok"


        print ('listening ...')
        recv_message = con.recv(1024).decode('utf-8') 
        print( recv_message )  
        split_msg = recv_message.split("_")
        if (len(split_msg)) >1 and isinstance(split_msg[1], int):
            
            CaliPos = int(split_msg[1])
            print (CaliPos)
        else:
            CaliPos = -1

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