import sys
from auth import MiBand3
from cursesmenu import *
from cursesmenu.items import *
from constants import ALERT_TYPES
import time
import serial
import os

### ADRES::: C3:2A:EC:6C:90:B9


def call_immediate():
    print 'Sending Call Alert'
    time.sleep(1)
    band.send_alert(ALERT_TYPES.PHONE)
def msg_immediate():
    print 'Sending Message Alert'
    time.sleep(1)
    band.send_alert(ALERT_TYPES.MESSAGE)
def detail_info():
    print 'MiBand'
    print 'Soft revision:',band.get_revision()
    print 'Hardware revision:',band.get_hrdw_revision()
    print 'Serial:',band.get_serial()
    print 'Battery:', band.get_battery_info()
    print 'Time:', band.get_current_time()
    print 'Steps:', band.get_steps()
    raw_input('Press Enter to continue')
def custom_message():
    band.send_custom_alert(5)

def custom_call():
    # custom_call
    band.send_custom_alert(3)

def custom_missed_call():
    band.send_custom_alert(4)
def l(x):
    print 'Realtime heart BPM:', x
    
    src=open("datas/heart_rate.txt","r")
    newData= str(x)+"\n"   
    oldData=src.readlines()
    oldData.insert(0,newData)
    src.close()
 
    src=open("datas/heart_rate.txt","w")
    src.writelines(oldData)
    src.close()




def heart_beat():
    band.start_raw_data_realtime(heart_measure_callback=l)
    raw_input('Press Enter to continue')

def change_date():
    band.change_date()
MAC_ADDR = sys.argv[1]
print 'Attempting to connect to ', MAC_ADDR

def updateFirmware():
    fileName = raw_input('Enter the file Name with Extension\n')
    band.dfuUpdate(fileName)

band = MiBand3(MAC_ADDR, debug=True)
band.setSecurityLevel(level = "medium")

# Authenticate the MiBand
if len(sys.argv) > 2:
    if band.initialize():
        print("Initialized...")
    band.disconnect()
    sys.exit(0)
else:
    band.authenticate()



if __name__ == "__main__":
    #getBodyHeat()
    band.get_steps()
    heart_beat()









