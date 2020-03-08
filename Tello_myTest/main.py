import tello
from tello_control_ui import TelloUI


def main():

    #drone = tello.Tello('192.168.10.2', 8889)  
    drone = tello.Tello('192.168.10.2', 80)
    vplayer = TelloUI(drone,"./img/")
    
	# start the Tkinter mainloop
    vplayer.root.mainloop() 

if __name__ == "__main__":
    main()
