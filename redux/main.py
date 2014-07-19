from  multiprocessing import Process
from btsub import BTSub
from hardware_module import HardwareModule
from blockly_webserver import WebServer

if __name__ == "__main__":
  queue = BTSub('saad')
  hm = HardwareModule(queue)
  ws = WebServer()
  print 'this should happen'
  Process(target=hm.start, args=()).start()
  Process(target=ws.start, args=()).start()
  print 'this happened'
