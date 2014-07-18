import zmq

class BTSub(object):
  def __init__(self, topic):
    ctx = zmq.Context()
    self.s = ctx.socket(zmq.SUB)
    self.s.connect('tcp://127.0.0.1:5555')
    self.s.setsockopt(zmq.SUBSCRIBE, topic)
  def subscribe(self, callback):
    while True:
      topic, msg = self.s.recv_multipart()
      callback(msg)