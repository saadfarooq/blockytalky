import zmq

class BTPub(object):
  def __init__(self):
    ctx = zmq.Context()
    self.s = ctx.socket(zmq.PUB)
    self.s.bind('tcp://127.0.0.1:5555')
  def publish(self, message):
    print 'Sending to queue'
    self.s.send_multipart(['saad', message])
