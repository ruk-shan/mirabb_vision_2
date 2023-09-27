import socket  
from signal import signal, SIGINT
from time import sleep  
  
# create and configure socket on local host  
serverSocket = socket.socket()  
# host = socket.gethostname()  
# host= '10.5.57.232'
# host ='10.5.57.138'
host ='192.168.12.70'
# host ='192.168.12.234'
port = 1026 #arbitrary port  
serverSocket.bind( ( host, port ) )  
serverSocket.listen( 1 )  
  
con, addr = serverSocket.accept()  
connected = True  
print( "connected to client" )

# send_message = ''
recv_message = 'YY'

#send robot pos to halcon
def get_robot_pos():
    #get robot poss from ABB
    robot__current_pos = 'p[0.1111,0.2222,0.3333,0.4,0.5,0.6]'
    return robot__current_pos

def move_robot_to_pos(pos):
    print("dummy robot moving")
    sleep(1)
    print(f"robot moved to {pos}")
    return True

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    serverSocket.close(); 
    exit(0)

signal(SIGINT, handler)
  
while True:  
    try:
        #resposing to recv_messages
        if (recv_message == b'Ball'):
            send_message = str(get_robot_pos())
            print ('received Ball')
            print ('moving robot for Calibration')

            # print(f'sending message....:{send_message}')
            # con.send( bytes(send_message, "UTF-8" ) ) 
        
        elif (recv_message == b'get_pos'):
            send_message = str(get_robot_pos())
            print ("received 'get_pos'")

            print(f'sending message....:{send_message}')
            con.send( bytes(send_message, "UTF-8" ) ) 

        elif (recv_message == b'Home'):
            send_message = str(get_robot_pos())
            print ("received 'home'")
            print ('moving robot to home')
        
        elif (recv_message == b'CaliPos_0'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_0'")
            print ('moving robot to CaliPos_0')
        
        elif (recv_message == b'CaliPos_1'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_1'")
            print ('moving robot to CaliPos_1')

        elif (recv_message == b'CaliPos_2'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_2'")
            print ('moving robot to CaliPos_2')     

        elif (recv_message == b'CaliPos_3'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_3'")
            print ('moving robot to CaliPos_3')

        elif (recv_message == b'CaliPos_4'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_4'")
            print ('moving robot to CaliPos_4')  
        
        elif (recv_message == b'CaliPos_5'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_5'")
            print ('moving robot to CaliPos_5')
        
        elif (recv_message == b'CaliPos_6'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_6'")
            print ('moving robot to CaliPos_6')

        elif (recv_message == b'CaliPos_7'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_7'")
            print ('moving robot to CaliPos_7')     

        elif (recv_message == b'CaliPos_8'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_8'")
            print ('moving robot to CaliPos_8')

        elif (recv_message == b'CaliPos_9'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_9'")
            print ('moving robot to CaliPos_9')  

        elif (recv_message == b'CaliPos_10'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_10'")
            print ('moving robot to CaliPos_10')
        
        elif (recv_message == b'CaliPos_11'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_11'")
            print ('moving robot to CaliPos_11')

        elif (recv_message == b'CaliPos_12'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_12'")
            print ('moving robot to CaliPos_12')     

        elif (recv_message == b'CaliPos_13'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_13'")
            print ('moving robot to CaliPos_13')

        elif (recv_message == b'CaliPos_14'):
            send_message = str(get_robot_pos())
            print ("received 'CaliPos_14'")
            print ('moving robot to CaliPos_14')  
    
        else:
            send_message = ''       


        # send wave to client  
        print ('listening ...')
        recv_message = con.recv( 1024 ) 
        # print( recv_message.decode("utf-8") )  
        print( recv_message  )  
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
  