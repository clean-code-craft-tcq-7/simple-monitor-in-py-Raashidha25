
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
  if ((95 <= temperature <= 102 )and (60 <= pulseRate <= 100 )and spo2 >= 90):
    print('Vitals are OK!')
    blinkoutput()
    return True
  if (95 > temperature > 102 ) :
    print('Temperature critical!')
  if 60 > pulseRate > 100:
    print('Pulse Rate is out of range!')
  if spo2 < 90:
    print('Oxygen Saturation out of range!')
  blinkoutput()
  return False
  
