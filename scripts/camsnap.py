#!/usr/bin/python3
from datetime import datetime
from picamera import PiCamera
from pytz import timezone
from twisted.internet import task, reactor

timeout = 60.0
camera = PiCamera()
log_fmt = "%H:%M %m-%d-%Y"
pic_fmt = "%H%M-%m%d%Y"

def capture():
    current_time = datetime.now(timezone('EST')).strftime(log_fmt)
    file_friendly = datetime.now(timezone('EST')).strftime(pic_fmt)
    camera.capture(f'/home/pydro/images/{file_friendly}.jpg')
    return (f"photo taken succesfully at {current_time}")

task_queue = task.LoopingCall(capture)
task_queue.start(timeout)

reactor.run()
