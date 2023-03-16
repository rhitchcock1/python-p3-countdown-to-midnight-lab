# your code goes here!
import time

def countdown( x = 10):
   
    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1                   
    return print("HAPPY NEW YEAR!")

def countdown_with_sleep(x = 10):
  
    time.sleep(5) 
    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1  
                       
    return print("HAPPY NEW YEAR!")




  