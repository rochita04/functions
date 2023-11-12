import time
print("the next line will print only afer a few seconds")
def delay(seconds):
    time.sleep(seconds)
    print("hello")
delay(2)
