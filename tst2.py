"""#!/usr/bin/python
from __future__ import print_function

from wifi import Cell, Scheme

# get all cells from the air
ssids = [cell.ssid for cell in Cell.all('wlan0')]

schemes = list(Scheme.all())
print(ssids)

for scheme in schemes:
    ssid = scheme.options.get('azerty123', scheme.options.get('GalaxyA10'))
    print("ss",ssid)
    if ssid in ssids:
        print('Connecting to %s' % ssid)
        scheme.activate()
        break
"""
"""import re
from wifi import Cell, Scheme
import wifi.subprocess_compat as subprocess
from wifi.utils import ensure_file_exists

def wifiscan():
   allSSID = [cell.ssid for cell in Cell.all('wlan0')]
   #allSSID = Cell.all('wlan0')
   print (allSSID )# prints all available WIFI SSIDs
   myssid= 'TDS FORMATION' # vivekHome is my wifi name
   print(myssid)
   for i in range(len(allSSID )):
        if str(allSSID [i]) == myssid:
                a = i
                myssidA = allSSID [a]
                print(myssidA,a)
                break
        else:
                print ("getout")

        # Creating Scheme with my SSID.
   allSSID2 = Cell.all('wlan0')[0]
   print(allSSID2)
   myssid= Scheme.for_cell('wlan0',allSSID2,'azert') # vive1234 is the password to my wifi myssidA is the wifi name 
   
   print (myssid)
   myssid.save()
   myssid.activate()

wifiscan() """

from wifi import Cell, Scheme
celll=Cell.all('wlan0')
scheme = Scheme.for_cell('wlan0', 'TDS FORMATION', celll)
