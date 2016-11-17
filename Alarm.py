import os
import time
from tkinter import *

def change_settings(first):
        if first==0:
                modifications=read_settings()
                ring=modifications[0]
                repeat=modifications[1]
        setting=open("settings.txt","w")
        setting.write("Edit the settings file.\n")
        if first:
                print ("Select alarm tone-")   
                new_ring= filedialog.askopenfilename()
                print (new_ring)
                setting.write("Alarm tone :-"+new_ring+"\n")
        else:
                print ("Current tone to be played for alarm- "+ring)
                print ("Change it?(Y/N) "),
                reaction=input()
                if reaction=="y" or reaction=="Y":
                        new_ring=filedialog.askopenfilename()
                        print (new_ring)
                        setting.write(“New Ring tone -"+new_ring+"\n")
                else:
                        setting.write("New Ring tone "+ring+"\n")
        if first:
                print ("Snooze time(mins.)-"),
                repeat=int(input())
                if repeat<1 or repeat>10:
                        check=0
                check=1
                while(check<1):
                        print ("The range for snooze time is 1 minute to 10 minutes.")
                        print ("Enter snooze time again :"),
                        repeat=int(input())
                        if repeat>=1 and repeat<=10:
                                check=1
                setting.write("Snooze time -"+str(repeat)+"\n")
        else:
                print ("Current snooze time  -"+str(repeat))
                print ("Change the snooze time? (Y/N) "),
                reaction=input()
                if reaction =="y" or reaction =="Y":
                        print ("Enter new snooze time -"),
                        repeat=int(input())
                        check = 1
                        while(check<1):
                                print ("Snooze time should be between 1  to 10 mins.")
                                print ("Enter snooze time again : "),
                                repeat=int(input())
                                if repeat>=1 and repeat<=10:
                                        check=1
                setting.write("Snooze time-"+str(repeat)+"\n")
        setting.close()
def create_setting():
        print ("Create Settings for your alarm clock.")
        change_setting(1)
def read_setting():
        try:
                setting=open("settings.txt","r")
        except:
                create_setting()
                setting=open("settings.txt","r")
        try:
                count=0
                for line in setting:
                        if count<2:
                                count=count+1
                        elif count==2:
                                ring=line
                                ring = ring.split(":")
                                ring[1]= ring[1].split()[0]
                                ring1= ring[-1].split("/")
                                ring = ring[1]+":"
                                ring1[-1]= ring1[-1].split("\\")[0]
                                if len(ring1)==1:
                                        ring = ring +"\\"+str(ring1[0])
                                else:
                                        for i in range(1,(len(ring1))):
                                                ring = ring +"\\"+str(ring1[i])
                                #print (ring)
                                # ring =( ring[0])
                                #print ("ring ="+ ring)
                                ring = ring.split("\n")[0]
                                count=count+1
                                #print (count, ring)
                        elif count==3: 
                                repeat=line
                                repeat = repeat.split(":")
                                repeat = repeat[1].split()
                                repeat =int(repeat[0])
                                #print (count, repeat)
                return [tone, repeat]
        except Exception as x:
                print (count,x)
                print ("Error in settings file.")
                print ("Create settings file again.")
                create_settings()
                read_settings()
def ring(ring,repeat):
        while 1:
                os.startfile(ring)
                time.sleep(repeat *60)
                print ("Wake up!!!")


def main():
        print ("Simple alarm clock")
        print ("Do you want to change settings? (Y/N) "),
        reaction=input()
        if reaction=="y" or reaction=="Y":
                change_setting(0)
        modifications=read_setting()
        print ("Set  alarm time: ")
        print (" HH : "),
        hours=int(input())
        check = 0
        if hours<0 or hours>23:
                check = -1
        while check<0:
                print (" Hours don’t exist, enter again- "),
                hours=int(input())
                if hours<0 or hours>24:
                        check = -1
                else:
                        check = 0
        print (" MM : "),
        min=int(input())
        check = 0
        if min<0 or min>59:
                check = -1
        while check<0:
                print (" Minutes don’t exist, enter again- "),
                min=int(input())
                if min<0 or min>24:
                        check = -1
                else:
                        check = 0
        sys_time=time.ctime()
        sys_time=sys_time.split()
        sys_time=sys_time[3].split(":")
        sys_hours=int(sys_time[0])
        sys_min=int(sys_time[1])
        if hours<sys_hours:
                minutes=(60-sys_min)+min
                hh=(23-sys_hh)+hours
        elif hours==sys_hours:
                if min<sys_min:
                        hh=23
                        minutes=(60-sys_min)+min
                else:
                        hh=0
                        minutes=mm-sys_mm
        else:
                hh=hours-sys_hours-1
                minutes=(60-sys_min)+min
        if minutes >60:
                hh=hh+1
                minutes=minutes-60
        elif minutes<0:
                hh=hh-1
                minutes=minutes+60
        print ("Alarm will ring after "+str(hh)+" hours and "+str(minutes)+" minutes.")
        seconds=(hh*3600)+(minutes*60)   
        time.sleep(seconds)
        print ("wake up!!!")
        ring(modifications[0],modifications[1])


if __name__=='__main__':
        main()
