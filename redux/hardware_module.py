from btsub import BTSub

class HardwareModule(object):
    # Init hardware status and name, declare queues for the hardware, inits hardware
    def __init__(self, queue):
      self.queue = queue
      # queue.subscribe(self.hw_callback)
    def start(self):
      self.queue.subscribe(self.hw_callback)

    def hw_callback(self, msg):
      print msg

    