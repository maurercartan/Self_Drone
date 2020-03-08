# -*- coding:utf-8 -*-
from tello import Tello
import sys,os
from datetime import datetime
import time

def print_log(log):
    for stat in log:
        stat.print_stats()
        str = stat.return_stats()
        print str

if __name__=="__main__":
    tello = Tello()
    tello.send_command("command")
    
    input_cmd = ""
    while True:
        print "a-�_��(takeoff)"
        print "b-����(land)"
        print "c-�V�W����50����(up 50)"
        print "d-�V�U����50����(down 50)"
        print "e-�V������50����(left 50)"
        print "f-�V�k����50����(right 50)"
        print "g-�V�e����50����(forward 50)"
        print "h-�V�᭸��50����(back 50)"
        print "i-���ɰw50��(cw 50)"
        print "j-�f�ɰw50��(ccw 50)"
        print "k-�V��½��(flip l)"
        print "l-���V�y��(100,100,100)(go 100 100 100 50)"
        print "m-���V�y��(100,100,100)�P(500,500,500)(curve 100 100 100 500 500 500 50)"
        print "exit-�h�X"
        input_cmd = raw_input("�п�J���O:")
        if input_cmd=="exit":
            tello.send_command("land")
            break
        print input_cmd
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
            print_log(tello.get_log())
            input_cmd = ""
        os.system("cls")