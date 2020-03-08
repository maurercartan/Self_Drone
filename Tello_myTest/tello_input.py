# -*- coding:utf-8 -*-
from tello import Tello
import sys,os
from datetime import datetime
import time
import share
import threading

def videoLoop(tello):
    """
    The mainloop thread of Tkinter 
    Raises:
        RuntimeError: To get around a RunTime error that Tkinter throws due to threading.
    """
    try:
        # start the thread that get GUI image and drwa skeleton 
        time.sleep(0.5)
        tello.sending_command_thread.start()
        while not tello.stopEvent.is_set():                
            system = platform.system()

        # read the frame for GUI show
            frame = tello.tello.read()
            print(frame)
            share.face(frame)
            if frame is None or frame.size == 0:
                continue 
        
        # transfer the format from frame to image         
            image = Image.fromarray(frame)

        # we found compatibility problem between Tkinter,PIL and Macos,and it will 
        # sometimes result the very long preriod of the "ImageTk.PhotoImage" function,
        # so for Macos,we start a new thread to execute the _updateGUIImage function.
            if system =="Windows" or system =="Linux":                
                tello._updateGUIImage(image)

            else:
                thread_tmp = threading.Thread(target=tello._updateGUIImage,args=(image,))
                thread_tmp.start()
                time.sleep(0.03)                                                            
    except RuntimeError, e:
        print("[INFO] caught a RuntimeError")

if __name__=="__main__":
    #tello = Tello('192.168.10.2', 8889)
    tello = Tello('192.168.10.2', 80)
    tello.send_command("command")
    
    thread = threading.Thread(target=videoLoop, args=(tello))
    thread.start()
    
    input_cmd = ""
    while True:
        print("a-起飛(takeoff)")
        print("b-降落(land)")
        print("c-向上飛行50公分(up 50)")
        print("d-向下飛行50公分(down 50)")
        print("e-向左飛行50公分(left 50)")
        print("f-向右飛行50公分(right 50)")
        print("g-向前飛行50公分(forward 50)")
        print("h-向後飛行50公分(back 50)")
        print("i-順時針50度(cw 50)")
        print("j-逆時針50度(ccw 50)")
        print("k-向左翻轉(flip l)")
        print("l-飛向座標(100,100,100)(go 100 100 100 50)")
        print("m-飛向座標(100,100,100)與(500,500,500)(curve 100 100 100 500 500 500 50)")
        print("exit-退出")
        input_cmd = raw_input("請輸入指令:")
        if input_cmd=="exit":
            tello.send_command("land")
            break
        if input_cmd!="":
            if input_cmd=="a":
                tello.send_command("takeoff")
            elif input_cmd=="b":
                tello.send_command("land")
            elif input_cmd=="c":
                tello.send_command("up 50")
            elif input_cmd=="d":
                tello.send_command("down 50")
            elif input_cmd=="e":
                tello.send_command("left 50")
            elif input_cmd=="f":
                tello.send_command("right 50")
            elif input_cmd=="g":
                tello.send_command("forward 50")
            elif input_cmd=="h":
                tello.send_command("back 50")
            elif input_cmd=="i":
                tello.send_command("cw 50")
            elif input_cmd=="j":
                tello.send_command("ccw 50")
            elif input_cmd=="k":
                tello.send_command("flip l")
            elif input_cmd=="l":
                tello.send_command("go 100 100 100 50")
            elif input_cmd=="m":
                tello.send_command("curve 100 100 100 500 500 500 50")
            else:
                tello.send_command(input_cmd)
            input_cmd = ""
        os.system("cls")