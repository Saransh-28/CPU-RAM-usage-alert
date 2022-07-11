import time
import psutil
from winotify import Notification , audio


while True:
    cpu = psutil.cpu_percent()
    v_m = psutil.virtual_memory().percent
    if cpu > 70:
        toaster = Notification(app_id='CPU & RAM alert script' , 
                                title='CPU',
                                msg = 'CPU USAGE IS MORE THAN THRESHOLD',
                                duration='short')
        toaster.set_audio(audio.Default,loop=False)
        toaster.show()
    if v_m > 70:
        toaster = Notification(app_id='CPU & RAM alert script' , 
                                title='RAM',
                                msg = 'RAM USAGE IS MORE THAN THRESHOLD',
                                duration='short')
        toaster.set_audio(audio.Default,loop=False)
        toaster.show()      
    time.sleep(3)
