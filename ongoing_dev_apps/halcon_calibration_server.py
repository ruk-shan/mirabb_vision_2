import socket  
from time import sleep
import config 
import json
from getkey import getkey, key
from colorama import Fore
  
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
    val_to_return = config.robot_poses[line] 
    print ("robot_pose" + val_to_return)
    return val_to_return


def move_robot_to_pos(pos):
    print(Fore.GREEN +"     Press enter after, the robot moved to pos_" + str(pos))
    while True:
    # Get the pressed key
        var = getkey()
    # Print the pressed key
        if var == key.ENTER:
        # If the ENTER key is pressed, break the While loop.
            print(Fore.BLUE +"     You've pressed enter, Hope the robot is at pos_" + str(pos))
            print (Fore.WHITE)
            break  
    return True


while True:  
    try:

        #resposing to recv_messages
        if (recv_message == 'Ball'):
            print ('received Ball')
            sleep(.5)
            con.send( bytes("ok","UTF-8" ) ) 
            print ('sent msg : ok')
            sleep(.5)

        elif (recv_message == 'get_pos'):
            print("getting robot pose_"+ str(CaliPos))
            send_message = get_robot_pos(CaliPos)
            sleep(.5)
            print(f'sending message....:{send_message}')
            con.send( bytes(send_message, "UTF-8" ) ) 
            sleep(.5)

        elif (recv_message == 'Home'):
            print ("received 'home'")
            sleep(.5)
            con.send( bytes("ok, moved to home.", "UTF-8" ) ) 
            sleep(.5)
        
        elif (recv_message == 'DONE'):
            print ("I'm done, Bye")
            break
        
        elif (CaliPos >-1):
            print ("received CaliPos"+ str(CaliPos))
            move_robot_to_pos(CaliPos)
            sleep(.5)
            con.send( bytes("ok, moved to CaliPos_"+ str(CaliPos), "UTF-8" ) ) 
            sleep(.5)
        
        else:
            send_message = "ok"


        print ('listening ...')
        recv_message = con.recv(1024).decode('utf-8') 
        split_msg = recv_message.split("_")
        if (len(split_msg)) >1 and split_msg[0]== "CaliPos":
            CaliPos = int(split_msg[1])
            # print (f"CaliPos: {CaliPos}")


    except  socket.error: 
        con, addr = serverSocket.accept()  
        print( "connection lost... reconnecting" )  

        while not connected:  
            # attempt to reconnect, otherwise sleep for 2 seconds  
            try:  
                con, addr = serverSocket.accept()   
                connected = True  
                print( "re-connection successful" )  
            except socket.error:  
                sleep( 2 )  

con.close();  