import time

seconds=input("enter the time in seconds")

def countdown(seconds):
    while seconds:
          mins=int(seconds/60)
          secs = int(seconds%60)
          timer = f"{mins}:{secs}"
          seconds-=1
          time.sleep(1)
          print(timer)
          
countdown(int(seconds))

print("times up!!!!")