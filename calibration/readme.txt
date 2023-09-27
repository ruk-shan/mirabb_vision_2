
Before start the code...
    install required packages 
        pip install getkey
    chanhe config
        open config.py and change the IP and PORT. IP is the host ip of the server. 
    add robot waypoints
        add robot waypoints list to the config.py follow the same format. 
    ABB robot code preparation 
        ABB shoud have a 15 waypoints that robot can be moved manualy. No TCP client required.

Running the code
    Start the halcon_calibration_server.py
    Start halcon calibration code

    When the server promts message on the terminal asking to move the robot, move ABB to waypoint 1 (must be matched with pos in the config.py file) and press enter. 
    Repeat this process for all 15 points.     
