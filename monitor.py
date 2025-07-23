
from time import sleep
import sys




def blinkoutput():
  for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)
      
def vitals_ok(temperature, pulseRate, spo2):
  
  vitals = {
    "Temperature": (temperature, 95, 102),
    "Pulse Rate": (pulseRate, 60, 100),
    "SpO2": (spo2, 90, 100)
   }

  for name,(value, min, max) in vitals.items():
    if not(min <= value <=max):
       print(f"{name} is out of range!")
       blinkoutput()
       return False
  
  print('Vitals are OK!')
  blinkoutput()
  return True
  
